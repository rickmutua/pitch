"""v1.2.5

Revision ID: 36806bb4bec8
Revises: 15a814e52a2b
Create Date: 2017-10-31 12:16:30.970127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36806bb4bec8'
down_revision = '15a814e52a2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('name', sa.String(length=255), nullable=True))
    op.drop_column('categories', 'category_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('category_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('categories', 'name')
    # ### end Alembic commands ###