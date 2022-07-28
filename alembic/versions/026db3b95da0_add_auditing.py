"""Add auditing

Revision ID: 026db3b95da0
Revises: e1444e3ae5e2
Create Date: 2022-07-28 11:04:37.152710

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "026db3b95da0"
down_revision = "e1444e3ae5e2"
branch_labels = None
depends_on = None


def upgrade():
    op.execute("select audit.enable_tracking('public.financial_performance'::regclass)")
    op.execute("select audit.enable_tracking('public.power_decision'::regclass)")
    op.execute("select audit.enable_tracking('public.power_impact'::regclass)")
    op.execute("select audit.enable_tracking('public.power_product'::regclass)")
    op.execute("select audit.enable_tracking('public.power'::regclass)")
    op.execute("select audit.enable_tracking('public.power_schedule'::regclass)")
    op.execute("select audit.enable_tracking('public.project_contact'::regclass)")
    op.execute("select audit.enable_tracking('public.project_data'::regclass)")
    op.execute("select audit.enable_tracking('public.project_document'::regclass)")
    op.execute("select audit.enable_tracking('public.project_investment'::regclass)")
    op.execute("select audit.enable_tracking('public.project_legal'::regclass)")
    op.execute("select audit.enable_tracking('public.project_market'::regclass)")
    op.execute("select audit.enable_tracking('public.project_partner'::regclass)")
    op.execute("select audit.enable_tracking('public.project'::regclass)")
    op.execute("select audit.enable_tracking('public.project_document'::regclass)")
    op.execute("select audit.enable_tracking('public.project_team'::regclass)")
    op.execute("select audit.enable_tracking('public.risk_management'::regclass)")
    op.execute("select audit.enable_tracking('public.sponsor'::regclass)")


def downgrade():
    pass
