"""empty message

Revision ID: 48de80cc240f
Revises: dd5b395b8792
Create Date: 2025-01-18 13:04:19.300382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48de80cc240f'
down_revision = 'dd5b395b8792'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
