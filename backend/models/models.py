from datetime import datetime
from backend.database import db
from sqlalchemy.dialects.mysql import INTEGER

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(INTEGER(unsigned=True), primary_key=True, nullable=False, autoincrement=True)
  username = db.Column(db.String(255), nullable=False)
  password = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), nullable=False, unique=True)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  delete_flg = db.Column(db.Boolean, nullable=False, default=True)
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
  title = db.Column(db.String(255), nullable=True)
  show = db.Column(db.Boolean, nullable=False, default=True, server_default="true")
  done = db.Column(db.Boolean, nullable=False, default=False, server_default="false")
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  limit_at = db.Column(db.Date)
  sub_tasks = db.relationship('Subtask',backref=db.backref('task',lazy=True))

  def __repr__(self):
    return f'<Task {self.id} {self.title}>'

  def toDict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'title': self.title,
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
  title = db.Column(db.String(255), nullable=True)
  show = db.Column(db.Boolean, nullable=False, default=True, server_default="true")
  done = db.Column(db.Boolean, nullable=False, default=False, server_default="false")
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  limit_at = db.Column(db.Date)

  def __repr__(self):
    return f'<Subtask {self.id} {self.title}>'

  def toDict(self):
    return {
      'id': self.id,
      'user_id': self.user_id,
      'task_id': self.task_id,
      'title': self.title,
      'show': self.show,
      'done': self.done,
      'created_at': self.created_at,
      'limit_at': self.limit_at,
    }
