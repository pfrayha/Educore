"""empty message

Revision ID: b6522bf0ed65
Revises: 
Create Date: 2020-06-20 21:44:37.642633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6522bf0ed65'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guardians',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('cpf', sa.String(length=15), nullable=True),
    sa.Column('cellphone', sa.String(length=15), nullable=True),
    sa.Column('housephone', sa.String(length=15), nullable=True),
    sa.Column('address_number', sa.SmallInteger(), nullable=True),
    sa.Column('address_street', sa.String(length=100), nullable=True),
    sa.Column('address_complement', sa.String(length=50), nullable=True),
    sa.Column('address_neighborhood', sa.String(length=20), nullable=True),
    sa.Column('address_city', sa.String(length=20), nullable=True),
    sa.Column('address_uf', sa.CHAR(length=2), nullable=True),
    sa.Column('address_cep', sa.CHAR(length=8), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_guardians_email'), 'guardians', ['email'], unique=True)
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('guardian_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['guardian_id'], ['guardians.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=60),
               nullable=True)
    op.alter_column('users', 'password_hash',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.drop_constraint('users_email_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('users', 'password_hash',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=60),
               nullable=False)
    op.drop_table('students')
    op.drop_index(op.f('ix_guardians_email'), table_name='guardians')
    op.drop_table('guardians')
    # ### end Alembic commands ###
