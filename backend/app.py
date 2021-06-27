"""flask appの初期化を行い、flask appオブジェクトの実体を持つ"""
from flask import Flask

from backend.database import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.config.Config')

    init_db(app)

    return app

app = create_app()