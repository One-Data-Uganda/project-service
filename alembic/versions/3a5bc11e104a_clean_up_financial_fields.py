"""Clean up financial fields

Revision ID: 3a5bc11e104a
Revises: b4d08a512418
Create Date: 2022-05-26 21:50:55.186868

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "3a5bc11e104a"
down_revision = "b4d08a512418"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "financial_performance",
        sa.Column("average_annual_output", sa.Float(), nullable=True),
    )
    op.add_column(
        "financial_performance",
        sa.Column("capital_investment", sa.Float(), nullable=True),
    )
    op.add_column(
        "financial_performance",
        sa.Column("average_annual_net_revenue", sa.Float(), nullable=True),
    )
    op.drop_column("financial_performance", "annual_revenue")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "financial_performance",
        sa.Column(
            "annual_revenue",
            postgresql.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.drop_column("financial_performance", "average_annual_net_revenue")
    op.drop_column("financial_performance", "capital_investment")
    op.drop_column("financial_performance", "average_annual_output")
    # ### end Alembic commands ###
