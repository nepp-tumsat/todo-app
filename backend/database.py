from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db_uri = 'mysql+pymysql://user:password@localhost/todo_app?charset=utf8'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, db.ForeignKey('tasks.user_id'), primary_key=True, autoincrement=True)
  username = db.Column(db.Varchar)
  password = db.Column(db.Varchar)
  created_at = db.Column(db.Datetime)

class Task(db.Model):
  __tablename__ = 'tasks'
  id = db.Column(db.Integer, db.ForeignKey('sub_tasks.task_id'),primary_key=True, autoincrement=True)
  user_id = db.Column(db.Integer)
  limit_at = db.Column(db.Datetime)
  created_at = db.Column(db.Datetime)
  task = db.Column(db.Varcher)
  user = db.relationship('User',backref=db.backref('tasks',lazy=True))

class Subtask(db.Model):
  __tablename__ = 'sub_tasks'
  id = db.Column(db.Integer,primary_key=True, autoincrement=True)
  user_id = db.Column(db.Integer)
  task_id = db.Column(db.Integer)
  created_at = db.Column(db.Datetime)
  sub_task = db.Column(db.Varcher)
  user = db.relationship('User',backref=db.backref('sub_tasks',lazy=True))

@app.route('/')
def top():
  
  users = User.query.all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)