"""Add sponsor short name

Revision ID: 44574e6c7eda
Revises: f375f2300e6f
Create Date: 2022-07-20 18:30:08.849734

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "44574e6c7eda"
down_revision = "f375f2300e6f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("sponsor", sa.Column("short_name", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("sponsor", "short_name")
    # ### end Alembic commands ###
