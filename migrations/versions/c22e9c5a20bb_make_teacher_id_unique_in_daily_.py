"""make teacher id unique in daily constraint- so there's no multiple constraint for the same teacher

Revision ID: c22e9c5a20bb
Revises: f73289069641
Create Date: 2025-04-05 21:18:51.850419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c22e9c5a20bb'
down_revision = 'f73289069641'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('teacher_daily_constraint', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['teacher_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('teacher_daily_constraint', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
