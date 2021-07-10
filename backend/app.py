  
"""flask appの初期化を行い、flask appオブジェクトの実体を持つ"""
from flask import Flask, jsonify, request
from flask_cors import CORS

from backend.database import init_db
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
    response_object = {'status': tasks}
    # db処理
    print('request:', request)
    return jsonify(response_object)



    