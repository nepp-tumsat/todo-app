"""aaaa

Revision ID: c5058bc4988a
Revises: 87581366d7a9
Create Date: 2021-08-08 22:21:44.787837

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c5058bc4988a'
down_revision = '87581366d7a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sub_tasks', 'limit_at',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255),
               type_=sa.Date(),
               existing_nullable=True)
    op.alter_column('tasks', 'limit_at',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255),
               type_=sa.Date(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'limit_at',
               existing_type=sa.Date(),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255),
               existing_nullable=True)
    op.alter_column('sub_tasks', 'limit_at',
               existing_type=sa.Date(),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255),
               existing_nullable=True)
    # ### end Alembic commands ###