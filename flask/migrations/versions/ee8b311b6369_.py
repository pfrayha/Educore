"""empty message

Revision ID: ee8b311b6369
Revises: ceace16cc11d
Create Date: 2020-06-20 22:34:57.383892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee8b311b6369'
down_revision = 'ceace16cc11d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_type_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'users', 'user_types', ['user_type_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'user_type_id')
    # ### end Alembic commands ###
