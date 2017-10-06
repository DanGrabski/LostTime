"""series users

Revision ID: 4f0d9ad0f000
Revises: 722212d210e8
Create Date: 2017-10-05 17:15:07.566848

"""

# revision identifiers, used by Alembic.
revision = '4f0d9ad0f000'
down_revision = '722212d210e8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('series', sa.Column('ltuserid', sa.Integer(), nullable=True))
    op.add_column('series', sa.Column('replacedbyid', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('series', 'replacedbyid')
    op.drop_column('series', 'ltuserid')
    ### end Alembic commands ###
