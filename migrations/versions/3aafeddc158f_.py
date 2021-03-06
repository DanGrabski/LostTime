"""empty message

Revision ID: 3aafeddc158f
Revises: d86b698b871d
Create Date: 2016-10-10 13:45:32.221626

"""

# revision identifiers, used by Alembic.
revision = '3aafeddc158f'
down_revision = 'd86b698b871d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_class',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('eventid', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('shortname', sa.String(), nullable=True),
    sa.Column('scoremethod', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('person_result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('eventid', sa.Integer(), nullable=True),
    sa.Column('classid', sa.Integer(), nullable=True),
    sa.Column('sicard', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('bib', sa.String(), nullable=True),
    sa.Column('club_shortname', sa.String(), nullable=True),
    sa.Column('coursestatus', sa.String(), nullable=True),
    sa.Column('resultstatus', sa.String(), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.Column('position', sa.Integer(), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person_result')
    op.drop_table('event_class')
    ### end Alembic commands ###
