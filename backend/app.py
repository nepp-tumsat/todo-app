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

@app.route('/user/addsample')
#ユーザーのサンプルデータ
def adduser():
    user1 = User(id=1,username='user1',password='pass')
    db.session.add(user1)
    db.session.commit()

@app.route('/task/addsample')
#タスクのサンプルデータ
def addtask():
    task1 = Task(id=1,user_id =1,task = 'task1')
    db.session.add(task1)
    db.session.commit()

    response_object = {'message': 'Successfully Add user'}
    jsonify(response_object)

@app.route('/subtask/addsample')
#サブタスクのサンプルデータ
def addsubtask():
    subtask1 = Subtask(user_id=1,task_id=1,sub_task="subtask1")
    db.session.add(subtask1)
    db.session.commit()

@app.route('/user/delete/<int:id>')
def delete_user(id):
    db.session.query(User).filter(User.id==id).delete()
    db.session.commit()

    users = User.query.all()
    response_object = []
    for i in users:
        dict = {'id': i.id,'username':i.username,"password":i.password,"created_at":i.created_at,'tasks':i.tasks,"sub_tasks":i.sub_tasks}
        response_object.append(dict)
    return jsonify(response_object)

@app.route('/list', methods=['GET'])
def list_todo():
    tasks = Task.query.all()
    response_object = []
    for i in tasks:
        dict = {'id': i.id,'user_id':i.user_id,"created_at":i.created_at,"limit_at":i.limit_at,'task':i.task}
        response_object.append(dict)
    return jsonify(response_object)

@app.route('/task/create', methods=['POST'])
def create_todo():
    new_task = Task()
    # requestの辞書を取得
    request_dict = request.get_json()
    new_task.task = request_dict['task_name']
    new_task.user_id = 1
    db.session.add(new_task)
    db.session.commit()

    tasks = Task.query.all()
    response_object = []
    for i in tasks:
        dict = {'id': i.id,'user_id':i.user_id,"created_at":i.created_at,"limit_at":i.limit_at,'task':i.task,"sub_tasks":i.sub_tasks}
        response_object.append(dict)
    return jsonify(response_object)

@app.route('/task/edit/<int:id>', methods=['POST'])
def edit_todo(id):
    edit_task=Task.query.get(id)
    request_dict = request.get_json()
    edit_task.task = request_dict['task_name']
    edit_task.created_at = datetime.now()
    edit_task.limit_at = datetime.now()

    db.session.commit()

    tasks = Task.query.all()
    response_object = []
    for i in tasks:
        dict = {'id': i.id,'user_id':i.user_id,"created_at":i.created_at,"limit_at":i.limit_at,'task':i.task,"sub_tasks":i.sub_tasks}
        response_object.append(dict)
    return jsonify(response_object)

@app.route('/task/delete/<int:id>',methods=['DELETE'])
def delete_todo(id):
    db.session.query(Task).filter(Task.id==id).delete()
    db.session.commit()

    tasks = Task.query.all()
    response_object = []
    for i in tasks:
        dict = {'id': i.id,'user_id':i.user_id,"created_at":i.created_at,"limit_at":i.limit_at,'task':i.task,"sub_tasks":i.sub_tasks}
        response_object.append(dict)
    return jsonify(response_object)

@app.route('/subtask/create/<int:id>',methods=['POST'])
# タスクのidを指定してそれに関連付けたサブタスクを作る
def create_subtask(id):
    new_subtask = Subtask()
    request_dict = request.get_json()
    new_subtask.sub_task = request_dict['subtask_name']
    new_subtask.user_id = 1
    new_subtask.task_id = id

    db.session.add(new_subtask)
    db.session.commit()

    subtasks = Subtask.query.filter(Subtask.task_id == id)
    response_object = []
    for i in subtasks:
        dict = {'id': i.id,'user_id':i.user_id,'task_id':i.task_id,"created_at":i.created_at,"limit_at":i.limit_at,"sub_task":i.sub_task}
        response_object.append(dict)
    return jsonify(response_object)

@app.route('/subtask/edit/<int:taskid>/<int:id>', methods=['POST'])
def edit_subtask(taskid,id):
    edit_subtask=Subtask.query.get(id)
    request_dict = request.get_json()
    edit_subtask.sub_task = request_dict['subtask_name']
    edit_subtask.created_at = datetime.now()
    edit_subtask.limit_at = datetime.now()
    subtasks = Subtask.query.filter(Subtask.task_id == taskid)
    response_object = []
    for i in subtasks:
        dict = {'id': i.id,'user_id':i.user_id,'task_id':i.task_id,"created_at":i.created_at,"limit_at":i.limit_at,"sub_task":i.sub_task}
        response_object.append(dict)
    return jsonify(response_object)


