"""client_id

Revision ID: 4f2e278c5df3
Revises: 823dd71ea3fc
Create Date: 2023-02-25 11:57:46.179489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f2e278c5df3'
down_revision = '823dd71ea3fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('client_id', sa.Integer(), nullable=True))
        batch_op.create_unique_constraint(batch_op.f('uq_user_email'), ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_email'), type_='unique')
        batch_op.drop_column('client_id')

    # ### end Alembic commands ###