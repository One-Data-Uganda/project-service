"""Add tail

Revision ID: 26f0b46bd8ad
Revises: 70ce4bc948f2
Create Date: 2022-07-21 16:05:43.430447

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "26f0b46bd8ad"
down_revision = "70ce4bc948f2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("project_data", sa.Column("tail_type", sa.Text(), nullable=True))
    op.add_column("project_data", sa.Column("tail_length", sa.Float(), nullable=True))
    op.add_column("project_data", sa.Column("tail_width", sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("project_data", "tail_width")
    op.drop_column("project_data", "tail_length")
    op.drop_column("project_data", "tail_type")
    # ### end Alembic commands ###