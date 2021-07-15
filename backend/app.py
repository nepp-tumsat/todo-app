  
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
@app.route('/add')
def add():
    user1 = User(username='user1',password='pass')
    task1 = Task(user_id =1,task = 'task1')

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
    new_task.task = request.form['task']
    new_task.user_id = request.form['user_id']
    db.session.add(new_task)
    db.session.commit()
    
    tasks = Task.query.all()
    response_object = []
    for i in tasks:
        
        dict = {'id': i.id,'user_id':i.user_id,"created_at":i.created_at,"limit_at":i.limit_at,'task':i.task,"sub_tasks":i.sub_tasks}
        response_object.append(dict)
    
    return jsonify(response_object)

@app.route('/delete/<int:id>')
def delete_todo(id):
    destroy_task = Task.query.get(id)
    db.session.delete(destroy_task)
    db.session.commit()

    tasks = Task.query.all()
    response_object = []
    for i in tasks:
        
        dict = {'id': i.id,'user_id':i.user_id,"created_at":i.created_at,"limit_at":i.limit_at,'task':i.task,"sub_tasks":i.sub_tasks}
        response_object.append(dict)
    
    return jsonify(response_object)
    