from datetime import datetime
from backend.database import db

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, db.ForeignKey('tasks.user_id'), primary_key=True, autoincrement=True)
  username = db.Column(db.String(255))
  password = db.Column(db.String(255))
  created_at = db.Column(db.DateTime,nullable=False, default=datetime.now)

class Task(db.Model):
  __tablename__ = 'tasks'
  id = db.Column(db.Integer, db.ForeignKey('sub_tasks.task_id'),primary_key=True, autoincrement=True)
  user_id = db.Column(db.Integer)
  limit_at = db.Column(db.DateTime)
  created_at = db.Column(db.DateTime)
  task = db.Column(db.String(255))
  user = db.relationship('User',backref=db.backref('tasks',lazy=True))

class Subtask(db.Model):
  __tablename__ = 'sub_tasks'
  id = db.Column(db.Integer,primary_key=True, autoincrement=True)
  user_id = db.Column(db.Integer)
  task_id = db.Column(db.Integer)
  created_at = db.Column(db.DateTime)
  sub_task = db.Column(db.String(255))
  user = db.relationship('User',backref=db.backref('sub_tasks',lazy=True))

# @app.route('/')
# def top():
#   users = User.query.all()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80)