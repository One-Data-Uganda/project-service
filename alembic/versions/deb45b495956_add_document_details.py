"""Add document details

Revision ID: deb45b495956
Revises: b8ca18d810bc
Create Date: 2022-06-06 11:57:00.902924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'deb45b495956'
down_revision = 'b8ca18d810bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project_document', sa.Column('mimetype', sa.Text(), nullable=True))
    op.add_column('project_document', sa.Column('size', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project_document', 'size')
    op.drop_column('project_document', 'mimetype')
    # ### end Alembic commands ###
