  
"""flask appの初期化を行い、flask appオブジェクトの実体を持つ"""
from flask import Flask, jsonify, request
from flask_cors import CORS

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
@app.route('/addtask')
def addtask():
    task1 = Task(user_id =1,task = 'task1')
    db.session.add(task1)
    db.session.commit()

@app.route('/adduser')
def adduser():
    user1 = User(id=1,username='user1',password='pass')  
    db.session.add(user1)
    db.session.commit()

@app.route('/list', methods=['GET'])
def list_todo():
    
    
    tasks = Task.query.all()
    response_object = []
    for i in tasks:
        
        dict = {'id': i.id,'user_id':i.user_id,"created_at":i.created_at,"limit_at":i.limit_at,'task':i.task,"sub_tasks":i.sub_tasks}
        response_object.append(dict)
    # db処理
    # print('request:', request)
    return jsonify(response_object)


@app.route('/create', methods=['POST'])
def create_todo():
    new_task = Task()
    new_task.task = request.form['task_name']
    new_task.user_id = 1
    db.session.add(new_task)
    db.session.commit()
    
    tasks = Task.query.all()
    response_object = []
    for i in tasks:
        
        dict = {'id': i.id,'user_id':i.user_id,"created_at":i.created_at,"limit_at":i.limit_at,'task':i.task,"sub_tasks":i.sub_tasks}
        response_object.append(dict)
    
    return jsonify(response_object)

@app.route

@app.route('/delete/<int:id>')
def delete_todo(id):
    db.session.query(Task).filter(Task.id==id).delete()
    db.session.commit()

    tasks = Task.query.all()
    response_object = []
    for i in tasks:
        
        dict = {'id': i.id,'user_id':i.user_id,"created_at":i.created_at,"limit_at":i.limit_at,'task':i.task,"sub_tasks":i.sub_tasks}
        response_object.append(dict)
    
    return jsonify(response_object)

@app.route('/deleteuser/<int:id>')
def delete_user(id):
    db.session.query(User).filter(User.id==id).delete()
    db.session.commit()

    users = User.query.all()
    response_object = []
    for i in users:
        
        dict = {'id': i.id,'username':i.username,"password":i.password,"created_at":i.created_at,'tasks':i.tasks,"sub_tasks":i.sub_tasks}
        response_object.append(dict)
    
    return jsonify(response_object)
    