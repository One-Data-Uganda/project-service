"""Add project type

Revision ID: d73af65ba4e3
Revises: 3318a080e7c2
Create Date: 2022-05-19 08:35:35.767741

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "d73af65ba4e3"
down_revision = "3318a080e7c2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("project", sa.Column("type", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("project", "type")
    # ### end Alembic commands ###