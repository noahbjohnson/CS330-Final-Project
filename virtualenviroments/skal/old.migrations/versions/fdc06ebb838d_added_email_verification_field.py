"""added email verification field

Revision ID: fdc06ebb838d
Revises: 609968a09c80
Create Date: 2018-05-16 11:46:19.946466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdc06ebb838d'
down_revision = '609968a09c80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('verified', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'verified')
    # ### end Alembic commands ###
