"""Boolean型に変更

Revision ID: bc123abcfaa7
Revises: ee7a5a3b1c8e
Create Date: 2021-08-08 22:15:29.021352

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bc123abcfaa7'
down_revision = 'ee7a5a3b1c8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sub_tasks', 'limit_at',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)
    op.alter_column('tasks', 'limit_at',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'limit_at',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
    op.alter_column('sub_tasks', 'limit_at',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=True)
    # ### end Alembic commands ###
