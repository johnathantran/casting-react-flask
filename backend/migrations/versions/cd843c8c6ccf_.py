"""empty message

Revision ID: cd843c8c6ccf
Revises: 
Create Date: 2022-02-10 21:24:36.205114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd843c8c6ccf'
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
    op.alter_column('movies', 'releasedate',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('movies', 'releasedate',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
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
