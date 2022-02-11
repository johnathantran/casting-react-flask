"""init migration

Revision ID: 8e5c414c2481
Revises: 
Create Date: 2022-02-11 02:33:23.383753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e5c414c2481'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('actors', 'name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('actors', 'age',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('actors', 'gender',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('movies', 'title',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movies', 'title',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('actors', 'gender',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('actors', 'age',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('actors', 'name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###
