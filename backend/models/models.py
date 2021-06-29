from datetime import datetime
from backend.database import db
from sqlalchemy.dialects.mysql import INTEGER

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(INTEGER(unsigned=True), primary_key=True, nullable=False, autoincrement=True)
  username = db.Column(db.String(255), nullable=False, unique=True)
  password = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  tasks = db.relationship('Task',backref=db.backref('task',lazy=True))
  sub_tasks = db.relationship('Subtask',backref=db.backref('sub_task',lazy=True))

class Task(db.Model):
  __tablename__ = 'tasks'
  id = db.Column(INTEGER(unsigned=True), primary_key=True, nullable=False, autoincrement=True)
  user_id = db.Column(INTEGER(unsigned=True), db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  limit_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  task = db.Column(db.String(255), nullable=True)
  sub_tasks = db.relationship('Subtask',backref=db.backref('sub_task',lazy=True))

class Subtask(db.Model):
  __tablename__ = 'sub_tasks'
  id = db.Column(INTEGER(unsigned=True), primary_key=True, nullable=False, autoincrement=True)
  user_id = db.Column(INTEGER(unsigned=True), db.ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))
  task_id = db.Column(INTEGER(unsigned=True), db.ForeignKey('tasks.id', onupdate='CASCADE', ondelete='CASCADE'))
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  limit_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  sub_task = db.Column(db.String(255), nullable=True)
