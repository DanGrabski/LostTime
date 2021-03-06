"""empty message

Revision ID: cea70ae714bc
Revises: 58cf5bc7866e
Create Date: 2016-10-24 18:23:28.040625

"""

# revision identifiers, used by Alembic.
revision = 'cea70ae714bc'
down_revision = '58cf5bc7866e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('created', sa.DateTime(), nullable=True))
    op.add_column('event', sa.Column('host', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'host')
    op.drop_column('event', 'created')
    ### end Alembic commands ###
