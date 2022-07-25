"""Add investment description

Revision ID: 5cae80dab9ec
Revises: d9e813aa0e3d
Create Date: 2022-07-23 18:27:38.850258

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "5cae80dab9ec"
down_revision = "d9e813aa0e3d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "power", sa.Column("investment_description", sa.Text(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("power", "investment_description")
    # ### end Alembic commands ###