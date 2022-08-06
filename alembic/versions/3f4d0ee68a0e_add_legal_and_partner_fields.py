"""Add legal and partner fields

Revision ID: 3f4d0ee68a0e
Revises: 9c9758aac45d
Create Date: 2022-08-06 10:15:14.193273

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "3f4d0ee68a0e"
down_revision = "9c9758aac45d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "project_legal", sa.Column("sector_guidelines", sa.Text(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("project_legal", "sector_guidelines")
    # ### end Alembic commands ###
