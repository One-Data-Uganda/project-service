"""Add segment

Revision ID: fae45380e6e6
Revises: aeb01f9845c4
Create Date: 2022-06-21 20:28:10.099328

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "fae45380e6e6"
down_revision = "aeb01f9845c4"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("project", sa.Column("segment", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("project", "segment")
    # ### end Alembic commands ###
