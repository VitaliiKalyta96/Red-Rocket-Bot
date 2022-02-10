"""empty message

Revision ID: 0e95b8bee677
Revises:
Create Date: 2021-12-16 21:51:08.509253

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0e95b8bee677'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('title', sa.String(length=30), nullable=False))
    op.add_column('events', sa.Column('description', sa.String(length=100), nullable=False))
    op.add_column('events', sa.Column('date_time', sa.String(length=30), nullable=False))
    op.add_column('events', sa.Column('category', sa.String(length=100), nullable=False))
    op.add_column('events', sa.Column('link', sa.String(length=100), nullable=False))
    op.drop_column('events', 'date')
    op.drop_column('events', 'name_mentor')
    op.drop_column('events', 'time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('time', mysql.VARCHAR(length=100), nullable=False))
    op.add_column('events', sa.Column('name_mentor', mysql.VARCHAR(length=100), nullable=False))
    op.add_column('events', sa.Column('date', mysql.VARCHAR(length=100), nullable=False))
    op.drop_column('events', 'link')
    op.drop_column('events', 'category')
    op.drop_column('events', 'date_time')
    op.drop_column('events', 'description')
    op.drop_column('events', 'title')
    # ### end Alembic commands ###