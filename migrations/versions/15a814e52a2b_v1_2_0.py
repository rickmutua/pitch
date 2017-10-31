"""v1.2.0

Revision ID: 15a814e52a2b
Revises: a1ec5397ba48
Create Date: 2017-10-31 10:47:05.281838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15a814e52a2b'
down_revision = 'a1ec5397ba48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=255), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('category_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], name='category_pitch_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='category_pkey')
    )
    op.drop_table('categories')
    # ### end Alembic commands ###