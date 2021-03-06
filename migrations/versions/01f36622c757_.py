"""empty message

Revision ID: 01f36622c757
Revises: d2383353f59b
Create Date: 2016-10-28 22:34:30.025762

"""

# revision identifiers, used by Alembic.
revision = '01f36622c757'
down_revision = 'd2383353f59b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('club_code',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('namespace', sa.String(), nullable=True),
    sa.Column('code', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('club_code')
    ### end Alembic commands ###
