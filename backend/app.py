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

    return app

app = create_app()


#########
#API PATH#
#########
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/usersample',methods=['POST'])
#ユーザーのサンプルデータの追加
def usersample():
    sampleuser = User(username='sampleuser',password='pass')
    db.session.add(sampleuser)
    db.session.commit()

    response_object = {'message': 'Successfully Add SampleUser'}
    return jsonify(response_object)

@app.route('/tasksample',methods=['POST'])
#タスクのサンプルデータの追加
def tasksample():
    sampletask = Task(user_id=1,task = 'sampletask')
    db.session.add(sampletask)
    db.session.commit()

    response_object = {'message': 'Successfully Add SampleTask'}
    return jsonify(response_object)

@app.route('/subtasksample',methods=['POST'])
#サブタスクのサンプルデータの追加
def subtasksample():
    samplesubtask = Subtask(user_id=1,task_id=1,sub_task="samplesubtask")
    db.session.add(samplesubtask)
    db.session.commit()

    response_object = {'message': 'Successfully Add SampleSubtask'}
    return jsonify(response_object)

# @app.route('/user', methods=['POST'])
# def create_user():
#     new_user = User()
#     request_dict = request.get_json()
#     new_user.username = request_dict['user_name']
#     new_user.user_id = request_dict['password']
#     db.session.add(new_user)
#     db.session.commit()

#     users = User.query.all()
#     response_object = []
#     for user in users:
#         response_dict = {'id': user.id,
#                         'username':user.username,
#                         "password":user.password,
#                         "created_at":user.created_at
#                         }
#         response_object.append(response_dict)
#     return jsonify(response_object)

@app.route('/user/<int:id>',methods=['DELETE'])
def delete_user(id):
    db.session.query(User).filter(User.id==id).delete()
    db.session.commit()

    users = User.query.all()
    response_object = []
    for user in users:
        response_dict = {'id': user.id,
                        'username':user.username,
                        "password":user.password,
                        "created_at":user.created_at,
                        }
        response_object.append(response_dict)
    return jsonify(response_object)

# ここからtask
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

# @app.route('/task', methods=['POST'])
# def create_todo():
#     new_task = Task()
#     # requestの辞書を取得
#     request_dict = request.get_json()
#     new_task.task = request_dict['task_name']
#     new_task.user_id = request_dict['user_id']
#     db.session.add(new_task)
#     db.session.commit()

#     tasks = Task.query.all()
#     response_object = []
#     for task in tasks:
#         response_dict = {'id': task.id,
#                         'user_id':task.user_id,
#                         "created_at":task.created_at,
#                         "limit_at":task.limit_at,
#                         'task':task.task,
#                         }
#         response_object.append(response_dict)
#     return jsonify(response_object)

# @app.route('/task/<int:id>', methods=['PATCH'])
# def edit_todo(id):
#     edit_task=Task.query.get(id)
#     request_dict = request.get_json()
#     edit_task.task = request_dict['task_name']
#     edit_task.created_at = datetime.now()
#     edit_task.limit_at = datetime.now()

#     db.session.commit()

#     tasks = Task.query.all()
#     response_object = []
#     for task in tasks:
#         response_dict = {'id': task.id,
#                         'user_id':task.user_id,
#                         "created_at":task.created_at,
#                         "limit_at":task.limit_at,
#                         'task':task.task
#                         }
#         response_object.append(response_dict)
#     return jsonify(response_object)

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


# 以下subtask
@app.route('/<int:taskid>/subtask',methods=['GET'])
def subtask(taskid):
    subtasks = Subtask.query.filter(Subtask.task_id == taskid)
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

# @app.route('/<int:taskid>/subtask',methods=['POST'])
# def create_subtask(taskid):
#     new_subtask = Subtask()
#     request_dict = request.get_json()
#     new_subtask.sub_task = request_dict['subtask_name']
#     new_subtask.user_id = request_dict['user_id']
#     new_subtask.task_id = taskid

#     db.session.add(new_subtask)
#     db.session.commit()

#     subtasks = Subtask.query.filter(Subtask.task_id == id)
#     response_object = []
#     for subtask in subtasks:
#         response_dict = {'id': subtask.id,
#                         'user_id':subtask.user_id,
#                         'task_id':subtask.task_id,
#                         "created_at":subtask.created_at,"limit_at":subtask.limit_at,
#                         "sub_task":subtask.sub_task
#                         }
#         response_object.append(response_dict)
#     return jsonify(response_object)

# @app.route('/<int:taskid>/subtask/<int:id>', methods=['PATCH'])
# def edit_subtask(taskid,id):
#     edit_subtask=Subtask.query.get(id)
#     request_dict = request.get_json()
#     edit_subtask.sub_task = request_dict['subtask_name']
#     edit_subtask.limit_at = datetime.now()
#     subtasks = Subtask.query.filter(Subtask.task_id == taskid)
#     response_object = []
#     for subtask in subtasks:
#         response_dict = {'id': subtask.id,
#                         'user_id':subtask.user_id,
#                         'task_id':subtask.task_id,
#                         "created_at":subtask.created_at,"limit_at":subtask.limit_at,
#                         "sub_task":subtask.sub_task
#                         }
#         response_object.append(response_dict)
#     return jsonify(response_object)

# app.route('/<int:taskid>/subtask/<int:id>', methods=['DELETE'])
# def delete_subtask(taskid,id):
#     db.session.query(Subtask).filter(Subtask.id==id).delete()
#     db.session.commit()
#     subtasks = Subtask.query.filter(Subtask.task_id == taskid)
#     response_object = []
#     for subtask in subtasks:
#         response_dict = {'id': subtask.id,
#                         'user_id':subtask.user_id,
#                         'task_id':subtask.task_id,
#                         "created_at":subtask.created_at,"limit_at":subtask.limit_at,
#                         "sub_task":subtask.sub_task
#                         }
#         response_object.append(response_dict)
#     return jsonify(response_object)

