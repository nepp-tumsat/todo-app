"""flask appの初期化を行い、flask appオブジェクトの実体を持つ"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
from sqlalchemy.sql import case

from backend.database import init_db,db
from backend.models import User, Task, Subtask



def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.config.Config')
    init_db(app)
    return app

app = create_app()


#########
#API PATH#
#########
CORS(app, resources={r'/*': {'origins': '*'}})


#########
# LOGIN #
#########

# GETだとURLに情報が含まれる & キャッシュに残るため危険
@app.route('/login', methods=['POST'])
def login():
  request_dict = request.get_json()
  username = request_dict['user_name']
  password = request_dict['password']

  # SQLのANDはカンマ区切り
  # .all()を付けないとクエリが取得される
  # 参考: https://www.sukerou.com/2019/04/sqlalchemyandor.html
  user = db.session.query(User).filter(User.username==username, User.password==password).all()

  user_info = {}
  if len(user) == 1:
    status_code = 200
    message = 'Login Success'
    user_info = {
      'user_id': user[0].id,
      'user_name': user[0].username
    }
  else:
    # ヒットするユーザーが 0 or 2以上の場合
    status_code = 401
    message = 'Unauthorized' if len(user) == 0 else 'Internal Server error'

  response_object = {
    'message': message,
    'user_info': user_info
  }

  return jsonify(response_object), status_code


########
# USER #
########

@app.route('/user', methods=['GET'])
def list_user():
    users = User.query.all()
    response_object = []
    for user in users:
        response_dict = {'id': user.id,
                        'username':user.username,
                        'password':user.password,
                        "created_at":user.created_at,
                        "email":user.email,

                        }
        response_object.append(response_dict)

    return jsonify(response_object)

# userごとにtask一覧を返す
@app.route('/user/<int:user_id>/all_tasks', methods=['GET'])
def user_tasks(user_id):
    # Userのshow=Trueのtask_idのみ取得(まだmodelオブジェクト)
    db_task_ids = db.session.query(Task.id).filter(Task.user_id == user_id, Task.show==True).all()
    task_ids = [task_obj.id for task_obj in db_task_ids]
    # task取得
    user_tasks = db.session.query(Task).filter(Task.user_id == user_id, Task.show==True).all()
    user_subtasks = db.session.query(Subtask).filter(Subtask.user_id==user_id,
                                                    Subtask.task_id.in_(task_ids),
                                                    Subtask.show==True).all()

    res_tasks = []
    for task in user_tasks:
        res_tasks.append(task.toDict())

    res_subtasks = [subtask.toDict() for subtask in user_subtasks]

    return jsonify({
                    'tasks'   : res_tasks,
                    'subtasks': res_subtasks
                    })


@app.route('/user', methods=['POST'])
def create_user():
    new_user = User()
    request_dict = request.get_json()
    new_user.username = request_dict['user_name']
    new_user.password = request_dict['password']
    new_user.email = request_dict['email']

    # DBへ追加
    db.session.add(new_user)
    db.session.commit()

    response_dict = {'user_id': new_user.id,
                    'username':new_user.username,
                    'email':new_user.email}


    return jsonify(response_dict)

# UserテーブルのStatusを変更とかの方がいいかも
@app.route('/user/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
  status_code = 200
  response = {
    'message': ''
    }

  try:
    db.session.query(User).filter(User.id==user_id).delete()
    db.session.commit()

  except Exception as err:
    db.session.rollback()
    status_code = 500
    response['message'] = 'db error'

  else:
    response['message'] = 'Successfully Delete User'

  finally:
    db.session.close()
    return jsonify(response), status_code


########
# TASK #
########

@app.route('/task', methods=['GET'])
def list_todo():
    tasks = Task.query.all()
    response_object = []
    for task in tasks:
        response_dict = {'id': task.id,
                        'user_id':task.user_id,
                        "created_at":task.created_at,
                        "limit_at":task.limit_at,
                        'task':task.task,
                        }
        response_object.append(response_dict)
    return jsonify(response_object)

@app.route('/task', methods=['POST'])
def create_todo():
    new_task = Task()
    # requestの辞書を取得
    request_dict = request.get_json()
    new_task.task = request_dict['task_name']
    new_task.user_id = request_dict['user_id']
    db.session.add(new_task)
    db.session.commit()# ここでidが確定する

    res_obj = {
        'id': new_task.id,
        'user_id': new_task.user_id,
        'created_at': new_task.created_at,
        'limit_at': new_task.limit_at,
        'task': new_task.task,
        # 'sub_tasks': new_task.sub_tasks
    }
    return jsonify(res_obj)

@app.route('/task/<int:task_id>', methods=['PATCH'])
def update_edited_todo(task_id):
  status_code = 200
  res_obj = {
    'message' : '',
    'task_info' : {}
  }

  try:
    request_dict = request.get_json()
    edit_task = db.session.query(Task).filter(Task.id == task_id).first()
    edit_task.task = request_dict['task_name']
    db.session.commit()

  except Exception as err:
    db.session.rollback()
    status_code = 500
    res_obj['message'] = 'db error'

  else:
    res_obj['message'] = 'Edited Task!'
    task_info = {
      'id': edit_task.id,
      'created_at': edit_task.created_at,
      'limit_at': edit_task.limit_at,
      'title': edit_task.task,
      'done': edit_task.done
    }
    res_obj['task_info'] = task_info

  finally:
    db.session.close()
    return jsonify(res_obj), status_code

@app.route('/task/<int:task_id>/limit', methods=['PATCH'])
def add_limit(task_id):
  response = {
    'message' : '',
    'task_info' : {}
  }

  request_dict = request.get_json()
  limit_datetime = request_dict['limit_at']

  try:
    edit_task=Task.query.get(task_id)
    edit_task.limit_at = limit_datetime
    db.session.commit()

  except Exception as err:
    db.session.rollback()
    status_code = 500
    response['message'] = 'db error'

  else:
    response['task_info'] = {
        'id': edit_task.id,
        'created_at': edit_task.created_at,
        'limit_at': edit_task.limit_at,
        'title': edit_task.task,
    }
    response['message'] = 'success'
    status_code = 200

  finally:
    db.session.close()
    return jsonify(response), status_code

# showカラムをFalseにする
@app.route('/task/<int:task_id>/delete',methods=['PATCH'])
def hide_task(task_id):
  response = {
    'message' : ''
  }
  status_code = 200

  try:
    hide_task = db.session.query(Task).filter(Task.id == task_id).first()
    hide_task.show = False
    db.session.commit()

  except Exception as err:
    db.session.rollback()
    response['message'] = 'db error'
    status_code = 500

  else:
    response['task_info'] = hide_task.toDict()
    response['message'] = 'Deleted Task!'

  finally:
    db.session.close()
    return jsonify(response), status_code

@app.route('/task/<int:task_id>/completed',methods=['PATCH'])
def completed_task(task_id):
    completed_task=Task.query.get(task_id)
    completed_task.done=True
    db.session.commit()

    res_obj = {
        'id': delete_task.id,
        'user_id': delete_task.user_id,
        'created_at': delete_task.created_at,
        'limit_at': delete_task.limit_at,
        'task': delete_task.task,
        'done': completed_task.done,
        'show': delete_task.show
    }
    return jsonify(res_obj)

@app.route('/task/<int:task_id>',methods=['DELETE'])
def delete_todo(task_id):
    db.session.query(Task).filter(Task.id==task_id).delete()
    db.session.commit()

    tasks = Task.query.all()
    response_object = []
    for task in tasks:
        response_dict = {'id': task.id,
                        'user_id':task.user_id,
                        "created_at":task.created_at,
                        "limit_at":task.limit_at,
                        'task':task.task
                        }
        response_object.append(response_dict)
    return jsonify(response_object)


###########
# SUBTASK #
###########

@app.route('/task/<int:task_id>/subtasks',methods=['GET'])
def subtask(task_id):
    subtasks = Subtask.query.filter(Subtask.task_id == task_id)
    response_object = []
    for subtask in subtasks:
        response_dict = {'id': subtask.id,
                        'user_id':subtask.user_id,
                        'task_id':subtask.task_id,
                        "created_at":subtask.created_at,"limit_at":subtask.limit_at,
                        "sub_task":subtask.sub_task
                        }
        response_object.append(response_dict)
    return jsonify(response_object)

@app.route('/task/<int:task_id>/subtasks',methods=['POST'])
def create_subtask(task_id):
  request_dict = request.get_json()
  user_id = request_dict['user_id']
  sub_task_list = request_dict['subtasks']
  new_subtasks_list = [Subtask(
                    user_id = user_id,
                    task_id = subtask['task_id'],
                    sub_task = subtask['title']
                  ) for subtask in sub_task_list]

  # 複数追加
  status_code = 200
  response = {
    'message': '',
    'new_subtasks_arr':[]
  }

  try:
    db.session.add_all(new_subtasks_list)
    db.session.commit()

  except Exception as err:
    db.session.rollback()
    status_code = 500
    response['message'] = 'db error'
    return jsonify(response), status_code

  else:
    send_subtasks_list = [{
        'id' : subtask.id,
        'task_id' : subtask.task_id,
        'title' : subtask.sub_task,
        'done' : subtask.done
      } for subtask in new_subtasks_list]

    response['new_subtasks_arr'] = send_subtasks_list
    response['message'] = 'success'

  finally:
    db.session.close()
    return jsonify(response), status_code

# task_idは使ってないから/subtasks/だけでもいいかも？
@app.route('/task/<int:task_id>/subtasks/', methods=['PATCH'])
def update_edited_subtasks(task_id):
  request_dict = request.get_json()
  subtask_arr = request_dict['subtask_info']
  print('subtask_arr', subtask_arr)

  subtask_ids = list(map(lambda subtask: subtask['id'], subtask_arr))
  subtask_title_dict = { subtask['id']:subtask['title'] for subtask in subtask_arr}

  response = {}
  try:
    status_code = 200

    update_subtasks = db.session.query(Subtask).filter(
      Subtask.id.in_(subtask_ids)
    ).update({
      Subtask.sub_task: case(
        subtask_title_dict,
        value=Subtask.id, # valueにcaseで比較する列を指定
        else_=''
      )
    }, synchronize_session=False)

    print('update_subtasks', update_subtasks)

    db.session.commit()

  except Exception as err:
    db.session.rollback()
    status_code = 500
    response['message'] = 'db error'

  else:
    response['message'] = 'success'
    response['subtask_info'] = subtask_arr

  finally:
    db.session.close()
    return jsonify(response), status_code

@app.route('/task/<int:task_id>/subtasks/<int:subtask_id>', methods=['DELETE'])
def delete_subtask(task_id,subtask_id):
    db.session.query(Subtask).filter(Subtask.id==subtask_id).delete()
    db.session.commit()
    subtasks = Subtask.query.filter(Subtask.task_id == task_id)
    response_object = []
    for subtask in subtasks:
        response_dict = {'id': subtask.id,
                        'user_id':subtask.user_id,
                        'task_id':subtask.task_id,
                        "created_at":subtask.created_at,"limit_at":subtask.limit_at,
                        "sub_task":subtask.sub_task
                        }
        response_object.append(response_dict)
    return jsonify(response_object)

