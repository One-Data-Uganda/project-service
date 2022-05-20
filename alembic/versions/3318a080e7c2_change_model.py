"""Change model

Revision ID: 3318a080e7c2
Revises: 0daa8983e17b
Create Date: 2022-05-18 22:29:26.060615

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "3318a080e7c2"
down_revision = "0daa8983e17b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("project", sa.Column("development_model", sa.Text(), nullable=True))
    op.drop_constraint(
        "project_development_model_id_fkey", "project", type_="foreignkey"
    )
    op.drop_column("project", "development_model_id")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "project",
        sa.Column(
            "development_model_id",
            postgresql.UUID(),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.create_foreign_key(
        "project_development_model_id_fkey",
        "project",
        "development_model",
        ["development_model_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_column("project", "development_model")
    # ### end Alembic commands ###
