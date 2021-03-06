"""add time field

Revision ID: 9126267bc4b1
Revises: f405f9471bef
Create Date: 2021-12-24 17:53:52.167713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9126267bc4b1'
down_revision = 'f405f9471bef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_movement', sa.Column('dateOfMove', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product_movement', 'dateOfMove')
    # ### end Alembic commands ###
