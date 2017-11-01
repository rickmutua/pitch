"""v1.5.5

Revision ID: a789a22b9ba4
Revises: f5256e775801
Create Date: 2017-11-01 11:31:27.233969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a789a22b9ba4'
down_revision = 'f5256e775801'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitch', sa.Column('title', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitch', 'title')
    # ### end Alembic commands ###
