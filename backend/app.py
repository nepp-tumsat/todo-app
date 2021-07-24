"""flask appの初期化を行い、flask appオブジェクトの実体を持つ"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

from backend.database import init_db,db
from backend.models import User, Task, Subtask



def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.config.Config')
    init_db(app)
    with app.app_context():
        def add_sample():
            db.session.query(User).filter(User.id==1).delete()
            db.session.query(Task).filter(Task.id==1).delete()
            db.session.query(Subtask).filter(Subtask.id==1).delete()
            db.session.commit()
            sample_user = User(
                id=1,
                username='sampleuser',
                password='pass',
                email='email'
            )
            db.session.add(sample_user)
            sample_task = Task(
                id=1,
                user_id=1,
                task = 'sampletask')
            db.session.add(sample_task)
            sample_subtask = Subtask(
                id=1,
                user_id=1,
                task_id=1,
                sub_task="samplesubtask")
            db.session.add(sample_subtask)
            db.session.commit()
        add_sample()
    return app

app = create_app()


#########
#API PATH#
#########
CORS(app, resources={r'/*': {'origins': '*'}})

######################
# INSERT SAMPLE DATA #
######################

# @app.route('/usersample',methods=['POST'])
# #ユーザーのサンプルデータの追加
# def user_sample():
#     sample_user = User(
#         id=1,
#         username='sampleuser',
#         password='pass',
#         email='email'
#         )
#     db.session.add(sample_user)
#     db.session.commit()

#     response_object = {'message': 'Successfully Add SampleUser'}
#     return jsonify(response_object)

# @app.route('/tasksample',methods=['POST'])
# #タスクのサンプルデータの追加
# def task_sample():
#     sample_task = Task(id=1,user_id=1,task = 'sampletask')
#     db.session.add(sample_task)
#     db.session.commit()

#     response_object = {'message': 'Successfully Add SampleTask'}
#     return jsonify(response_object)

# @app.route('/subtasksample',methods=['POST'])
# #サブタスクのサンプルデータの追加
# def subtask_sample():
#     sample_subtask = Subtask(user_id=1,task_id=1,sub_task="samplesubtask")
#     db.session.add(sample_subtask)
#     db.session.commit()

#     response_object = {'message': 'Successfully Add SampleSubtask'}
#     return jsonify(response_object)

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
    message = 'Login Success'
    user_info = {
      'user_id': user[0].id,
      'user_name': user[0].username
    }
  else:
    # ヒットするユーザーが　0 or 2以上の場合
    message = 'Unauthorized' if len(user) == 0 else 'Internal Server error'

  response_object = {
    'message': message,
    'user_info': user_info
  }

  return jsonify(response_object)

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

@app.route('/user/<int:id>',methods=['DELETE'])
def delete_user(id):
    db.session.query(User).filter(User.id==id).delete()
    db.session.commit()
    response_object = {'message': 'Successfully Delete User'}
    return jsonify(response_object)


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
        'sub_tasks': new_task.sub_tasks
    }
    return jsonify(res_obj)

@app.route('/task/<int:id>', methods=['PATCH'])
def edit_todo(id):
    edit_task=Task.query.get(id)
    request_dict = request.get_json()
    edit_task.task = request_dict['task_name']

    db.session.commit()


    res_obj = {
        'id': edit_task.id,
        'user_id': edit_task.user_id,
        'created_at': edit_task.created_at,
        'limit_at': edit_task.limit_at,
        'task': edit_task.task,
        'sub_tasks': edit_task.sub_tasks
    }
    return jsonify(res_obj)

@app.route('/task/<int:id>/limit', methods=['PATCH'])
# [WIPS]
def add_limit(id):
    edit_task=Task.query.get(id)
    request_dict = request.get_json()
    edit_task.limit_at = datetime(request_dict['limit_at'])

    db.session.commit()

    res_obj = {
        'id': edit_task.id,
        'user_id': edit_task.user_id,
        'created_at': edit_task.created_at,
        'limit_at': edit_task.limit_at,
        'task': edit_task.task,
        'sub_tasks': edit_task.sub_tasks
    }
    return jsonify(res_obj)


@app.route('/task/<int:id>',methods=['DELETE'])
def delete_todo(id):
    db.session.query(Task).filter(Task.id==id).delete()
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

@app.route('/task/<int:task_id>/subtask',methods=['GET'])
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

@app.route('/task/<int:task_id>/subtask',methods=['POST'])
def create_subtask(task_id):
    new_subtask = Subtask()
    request_dict = request.get_json()
    new_subtask.sub_task = request_dict['subtask_name']
    new_subtask.user_id = request_dict['user_id']
    new_subtask.task_id = task_id

    db.session.add(new_subtask)
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

@app.route('/task/<int:task_id>/subtask/<int:subtask_id>', methods=['PATCH'])
def edit_subtask(task_id,subtask_id):
    edit_subtask=Subtask.query.get(subtask_id)
    request_dict = request.get_json()
    edit_subtask.sub_task = request_dict['subtask_name']
    edit_subtask.limit_at = datetime.now()
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

@app.route('/task/<int:task_id>/subtask/<int:subtask_id>', methods=['DELETE'])
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

