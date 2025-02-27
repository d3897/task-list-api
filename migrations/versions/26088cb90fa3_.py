"""empty message

Revision ID: 26088cb90fa3
Revises: 23629eb16eb0
Create Date: 2023-05-07 21:34:56.830585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26088cb90fa3'
down_revision = '23629eb16eb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('goal')
    op.alter_column('task', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('task', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('task', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_table('goal',
    sa.Column('goal_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('goal_id', name='goal_pkey')
    )
    # ### end Alembic commands ###
