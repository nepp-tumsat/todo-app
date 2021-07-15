  
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

