"""Add more project description fields

Revision ID: 78db9eab37e2
Revises: d8cceca3dd8a
Create Date: 2022-05-19 18:26:32.276313

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "78db9eab37e2"
down_revision = "d8cceca3dd8a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "project_investment", sa.Column("other_loan_types", sa.Text(), nullable=True)
    )
    op.add_column(
        "project_investment",
        sa.Column("other_loan_description", sa.Text(), nullable=True),
    )
    op.add_column(
        "project_investment", sa.Column("loan_amount", sa.Float(), nullable=True)
    )
    op.add_column(
        "project_investment", sa.Column("loan_mobilized", sa.Float(), nullable=True)
    )
    op.add_column(
        "project_investment",
        sa.Column("loan_needing_mobilization", sa.Float(), nullable=True),
    )
    op.add_column(
        "project_investment",
        sa.Column("proposed_grant_amount", sa.Text(), nullable=True),
    )
    op.add_column(
        "project_investment", sa.Column("grant_providers", sa.Text(), nullable=True)
    )
    op.add_column(
        "project_investment",
        sa.Column("prospective_grant_providers", sa.Text(), nullable=True),
    )
    op.add_column(
        "project_investment", sa.Column("grant_types", sa.Text(), nullable=True)
    )
    op.add_column(
        "project_investment", sa.Column("grant_amount", sa.Float(), nullable=True)
    )
    op.add_column(
        "project_investment", sa.Column("grant_mobilized", sa.Float(), nullable=True)
    )
    op.add_column(
        "project_investment",
        sa.Column("grant_needing_mobilization", sa.Float(), nullable=True),
    )
    op.add_column(
        "project_investment", sa.Column("total_mobilized", sa.Float(), nullable=True)
    )
    op.add_column(
        "project_investment",
        sa.Column("total_needing_mobilization", sa.Float(), nullable=True),
    )
    op.add_column(
        "project_investment",
        sa.Column("date_financial_close", sa.Date(), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("project_investment", "date_financial_close")
    op.drop_column("project_investment", "total_needing_mobilization")
    op.drop_column("project_investment", "total_mobilized")
    op.drop_column("project_investment", "grant_needing_mobilization")
    op.drop_column("project_investment", "grant_mobilized")
    op.drop_column("project_investment", "grant_amount")
    op.drop_column("project_investment", "grant_types")
    op.drop_column("project_investment", "prospective_grant_providers")
    op.drop_column("project_investment", "grant_providers")
    op.drop_column("project_investment", "proposed_grant_amount")
    op.drop_column("project_investment", "loan_needing_mobilization")
    op.drop_column("project_investment", "loan_mobilized")
    op.drop_column("project_investment", "loan_amount")
    op.drop_column("project_investment", "other_loan_description")
    op.drop_column("project_investment", "other_loan_types")
    # ### end Alembic commands ###