from datetime import datetime
from backend.database import db
from sqlalchemy.dialects.mysql import INTEGER

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(INTEGER(unsigned=True), primary_key=True, nullable=False, autoincrement=True)
  username = db.Column(db.String(255), nullable=False, unique=True)
  password = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), nullable=False, unique=True)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  tasks = db.relationship('Task',backref=db.backref('user',lazy=True))
  sub_tasks = db.relationship('Subtask',backref=db.backref('user',lazy=True))

  def __repr__(self):
    return f'<User {self.id} {self.username}>'

  def toDict(self):
    # pythonではself.xxxでクラス変数にアクセスできる
    return {
      'id': self.id,
      'username': self.username,
      'password': self.password,
      'email': self.email,
      'created_at': self.created_at,
    }

class Task(db.Model):
  __tablename__ = 'tasks'
  id = db.Column(INTEGER(unsigned=True), primary_key=True, nullable=False, autoincrement=True)
  user_id = db.Column(INTEGER(unsigned=True), db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))
  task = db.Column(db.String(255), nullable=True)
  show = db.Column(db.Boolean, nullable=False, default=True, server_default="true")
  done = db.Column(db.Boolean, nullable=False, default=False, server_default="false")
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  limit_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  sub_tasks = db.relationship('Subtask',backref=db.backref('task',lazy=True))

  def __repr__(self):
    return f'<Task {self.id} {self.task}>'

  def toDict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'task': self.task,
      'show': self.show,
      'done': self.done,
      'created_at': self.created_at,
      'limit_at': self.limit_at,
    }

class Subtask(db.Model):
  __tablename__ = 'sub_tasks'
  id = db.Column(INTEGER(unsigned=True), primary_key=True, nullable=False, autoincrement=True)
  user_id = db.Column(INTEGER(unsigned=True), db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))
  task_id = db.Column(INTEGER(unsigned=True), db.ForeignKey('tasks.id', onupdate='CASCADE', ondelete='CASCADE'))
  sub_task = db.Column(db.String(255), nullable=True)
  show = db.Column(db.Boolean, nullable=False, default=True, server_default="true")
  done = db.Column(db.Boolean, nullable=False, default=False, server_default="false")
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  limit_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

  def __repr__(self):
    return f'<Subtask {self.id} {self.sub_task}>'

  def toDict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'task_id': self.task_id,
      'sub_task': self.sub_task,
      'show': self.show,
      'done': self.done,
      'created_at': self.created_at,
      'limit_at': self.limit_at,
    }
