"""series processed

Revision ID: 498145c4934a
Revises: 4f0d9ad0f000
Create Date: 2017-10-05 17:18:08.971954

"""

# revision identifiers, used by Alembic.
revision = '498145c4934a'
down_revision = '4f0d9ad0f000'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('series', sa.Column('isProcessed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('series', 'isProcessed')
    ### end Alembic commands ###