"""4th

Revision ID: 705df9aab305
Revises: 434923401319
Create Date: 2018-09-03 22:18:33.749595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '705df9aab305'
down_revision = '434923401319'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###