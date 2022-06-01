"""Revise product fields

Revision ID: 394cfa521aad
Revises: f3d219950653
Create Date: 2022-06-01 01:10:34.211507

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "394cfa521aad"
down_revision = "f3d219950653"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "power_product",
        sa.Column("primary_customer_id", postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.create_foreign_key(
        None,
        "power_product",
        "power_customer",
        ["primary_customer_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_column("power_product", "primary_customer")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "power_product",
        sa.Column("primary_customer", sa.TEXT(), autoincrement=False, nullable=True),
    )
    op.drop_constraint(None, "power_product", type_="foreignkey")
    op.drop_column("power_product", "primary_customer_id")
    # ### end Alembic commands ###