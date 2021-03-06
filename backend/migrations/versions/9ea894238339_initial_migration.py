"""Initial migration

Revision ID: 9ea894238339
Revises: 
Create Date: 2019-11-11 06:05:25.933526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ea894238339'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dishes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=120), nullable=False),
    sa.Column('country', sa.String(length=120), nullable=False),
    sa.Column('category', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dishes_category'), 'dishes', ['category'], unique=False)
    op.create_index(op.f('ix_dishes_country'), 'dishes', ['country'], unique=False)
    op.create_index(op.f('ix_dishes_description'), 'dishes', ['description'], unique=False)
    op.create_index(op.f('ix_dishes_name'), 'dishes', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dishes_name'), table_name='dishes')
    op.drop_index(op.f('ix_dishes_description'), table_name='dishes')
    op.drop_index(op.f('ix_dishes_country'), table_name='dishes')
    op.drop_index(op.f('ix_dishes_category'), table_name='dishes')
    op.drop_table('dishes')
    # ### end Alembic commands ###
