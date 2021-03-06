"""empty message

Revision ID: 3e005cb77603
Revises: 715fc02cea3
Create Date: 2014-08-30 10:42:44.226375

"""

# revision identifiers, used by Alembic.
revision = '3e005cb77603'
down_revision = '715fc02cea3'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('record', sa.Column('note', mysql.TEXT(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('record', 'note')
    ### end Alembic commands ###
