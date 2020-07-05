"""empty message

Revision ID: b07b233e40bf
Revises: f213a7f83294
Create Date: 2020-07-04 20:54:34.275467

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b07b233e40bf'
down_revision = 'f213a7f83294'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pessoa', 'nome_responsavel',
               existing_type=postgresql.ARRAY(sa.VARCHAR(length=100)),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pessoa', 'nome_responsavel',
               existing_type=postgresql.ARRAY(sa.VARCHAR(length=100)),
               nullable=False)
    # ### end Alembic commands ###
