"""[first]

Revision ID: 3d7966086c03
Revises: 
Create Date: 2021-07-22 21:43:04.259288

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3d7966086c03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', mysql.INTEGER(unsigned=True), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('tasks',
    sa.Column('id', mysql.INTEGER(unsigned=True), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(unsigned=True), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('limit_at', sa.DateTime(), nullable=False),
    sa.Column('task', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sub_tasks',
    sa.Column('id', mysql.INTEGER(unsigned=True), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(unsigned=True), nullable=True),
    sa.Column('task_id', mysql.INTEGER(unsigned=True), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('limit_at', sa.DateTime(), nullable=False),
    sa.Column('sub_task', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sub_tasks')
    op.drop_table('tasks')
    op.drop_table('users')
    # ### end Alembic commands ###
