"""Add water services

Revision ID: f291a5fbfaac
Revises: fdf2aa8f2630
Create Date: 2022-05-26 12:14:07.985143

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "f291a5fbfaac"
down_revision = "fdf2aa8f2630"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "power",
        sa.Column("main_service_id", postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.add_column("power", sa.Column("other_services", sa.Text(), nullable=True))
    op.drop_constraint("power_capacity_id_fkey", "power", type_="foreignkey")
    op.drop_constraint("power_ppa_status_id_fkey", "power", type_="foreignkey")
    op.drop_constraint("power_unit_id_fkey", "power", type_="foreignkey")
    op.drop_constraint("power_technology_type_id_fkey", "power", type_="foreignkey")
    op.drop_constraint("power_energy_resource_id_fkey", "power", type_="foreignkey")
    op.drop_constraint("power_technology_id_fkey", "power", type_="foreignkey")
    op.drop_constraint("power_ppa_status_grid_id_fkey", "power", type_="foreignkey")
    op.drop_constraint("power_off_taker_id_fkey", "power", type_="foreignkey")
    op.create_foreign_key(
        None,
        "power",
        "technology_type",
        ["technology_type_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "power",
        "energy_resource",
        ["energy_resource_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "power",
        "ppa_status",
        ["ppa_status_grid_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "power",
        "water_service",
        ["main_service_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "power",
        "off_taker",
        ["off_taker_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "power",
        "ppa_status",
        ["ppa_status_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "power",
        "unit",
        ["unit_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "power",
        "technology",
        ["technology_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "power",
        "capacity",
        ["capacity_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "power_energy_resource_power_id_fkey",
        "power_energy_resource",
        type_="foreignkey",
    )
    op.drop_constraint(
        "power_energy_resource_energy_resource_id_fkey",
        "power_energy_resource",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "power_energy_resource",
        "energy_resource",
        ["energy_resource_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "power_energy_resource",
        "power",
        ["power_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "power_power_customer_power_id_fkey", "power_power_customer", type_="foreignkey"
    )
    op.drop_constraint(
        "power_power_customer_power_customer_id_fkey",
        "power_power_customer",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "power_power_customer",
        "power_customer",
        ["power_customer_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "power_power_customer",
        "power",
        ["power_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "power_product_product_service_id_fkey", "power_product", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "power_product",
        "product_service",
        ["product_service_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "power_water_service_water_service_id_fkey",
        "power_water_service",
        type_="foreignkey",
    )
    op.drop_constraint(
        "power_water_service_power_id_fkey", "power_water_service", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "power_water_service",
        "power",
        ["power_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "power_water_service",
        "water_service",
        ["water_service_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint("project_sponsor_type_id_fkey", "project", type_="foreignkey")
    op.drop_constraint("project_status_id_fkey", "project", type_="foreignkey")
    op.drop_constraint(
        "project_development_type_id_fkey", "project", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "project",
        "sponsor_type",
        ["sponsor_type_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "project",
        "status",
        ["status_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "project",
        "development_type",
        ["development_type_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "project_country_project_id_fkey", "project_country", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "project_country",
        "project",
        ["project_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "project_data_turbine_capacity_id_fkey", "project_data", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "project_data",
        "capacity",
        ["turbine_capacity_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "project_document_project_id_fkey", "project_document", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "project_document",
        "project",
        ["project_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "project_region_project_id_fkey", "project_region", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "project_region",
        "project",
        ["project_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "project_sponsor_type_sponsor_type_id_fkey",
        "project_sponsor_type",
        type_="foreignkey",
    )
    op.drop_constraint(
        "project_sponsor_type_sponsor_id_fkey",
        "project_sponsor_type",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "project_sponsor_type",
        "sponsor",
        ["sponsor_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "project_sponsor_type",
        "sponsor_type",
        ["sponsor_type_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "project_type_project_id_fkey", "project_type", type_="foreignkey"
    )
    op.drop_constraint("project_type_type_id_fkey", "project_type", type_="foreignkey")
    op.create_foreign_key(
        None,
        "project_type",
        "project",
        ["project_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.create_foreign_key(
        None,
        "project_type",
        "ptype",
        ["type_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "sponsor_country_sponsor_id_fkey", "sponsor_country", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "sponsor_country",
        "sponsor",
        ["sponsor_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "sponsor_document_sponsor_id_fkey", "sponsor_document", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "sponsor_document",
        "sponsor",
        ["sponsor_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "sponsor_sector_industry_sponsor_id_fkey",
        "sponsor_sector_industry",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "sponsor_sector_industry",
        "sponsor",
        ["sponsor_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    op.drop_constraint(
        "technology_type_technology_id_fkey", "technology_type", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "technology_type",
        "technology",
        ["technology_id"],
        ["id"],
        onupdate="RESTRICT",
        ondelete="RESTRICT",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "technology_type", type_="foreignkey")
    op.create_foreign_key(
        "technology_type_technology_id_fkey",
        "technology_type",
        "technology",
        ["technology_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "sponsor_sector_industry", type_="foreignkey")
    op.create_foreign_key(
        "sponsor_sector_industry_sponsor_id_fkey",
        "sponsor_sector_industry",
        "sponsor",
        ["sponsor_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "sponsor_document", type_="foreignkey")
    op.create_foreign_key(
        "sponsor_document_sponsor_id_fkey",
        "sponsor_document",
        "sponsor",
        ["sponsor_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "sponsor_country", type_="foreignkey")
    op.create_foreign_key(
        "sponsor_country_sponsor_id_fkey",
        "sponsor_country",
        "sponsor",
        ["sponsor_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "project_type", type_="foreignkey")
    op.drop_constraint(None, "project_type", type_="foreignkey")
    op.create_foreign_key(
        "project_type_type_id_fkey",
        "project_type",
        "ptype",
        ["type_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "project_type_project_id_fkey",
        "project_type",
        "project",
        ["project_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "project_sponsor_type", type_="foreignkey")
    op.drop_constraint(None, "project_sponsor_type", type_="foreignkey")
    op.create_foreign_key(
        "project_sponsor_type_sponsor_id_fkey",
        "project_sponsor_type",
        "sponsor",
        ["sponsor_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "project_sponsor_type_sponsor_type_id_fkey",
        "project_sponsor_type",
        "sponsor_type",
        ["sponsor_type_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "project_region", type_="foreignkey")
    op.create_foreign_key(
        "project_region_project_id_fkey",
        "project_region",
        "project",
        ["project_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "project_document", type_="foreignkey")
    op.create_foreign_key(
        "project_document_project_id_fkey",
        "project_document",
        "project",
        ["project_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "project_data", type_="foreignkey")
    op.create_foreign_key(
        "project_data_turbine_capacity_id_fkey",
        "project_data",
        "capacity",
        ["turbine_capacity_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "project_country", type_="foreignkey")
    op.create_foreign_key(
        "project_country_project_id_fkey",
        "project_country",
        "project",
        ["project_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "project", type_="foreignkey")
    op.drop_constraint(None, "project", type_="foreignkey")
    op.drop_constraint(None, "project", type_="foreignkey")
    op.create_foreign_key(
        "project_development_type_id_fkey",
        "project",
        "development_type",
        ["development_type_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "project_status_id_fkey",
        "project",
        "status",
        ["status_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "project_sponsor_type_id_fkey",
        "project",
        "sponsor_type",
        ["sponsor_type_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "power_water_service", type_="foreignkey")
    op.drop_constraint(None, "power_water_service", type_="foreignkey")
    op.create_foreign_key(
        "power_water_service_power_id_fkey",
        "power_water_service",
        "power",
        ["power_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "power_water_service_water_service_id_fkey",
        "power_water_service",
        "water_service",
        ["water_service_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "power_product", type_="foreignkey")
    op.create_foreign_key(
        "power_product_product_service_id_fkey",
        "power_product",
        "product_service",
        ["product_service_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="SET NULL",
    )
    op.drop_constraint(None, "power_power_customer", type_="foreignkey")
    op.drop_constraint(None, "power_power_customer", type_="foreignkey")
    op.create_foreign_key(
        "power_power_customer_power_customer_id_fkey",
        "power_power_customer",
        "power_customer",
        ["power_customer_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "power_power_customer_power_id_fkey",
        "power_power_customer",
        "power",
        ["power_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "power_energy_resource", type_="foreignkey")
    op.drop_constraint(None, "power_energy_resource", type_="foreignkey")
    op.create_foreign_key(
        "power_energy_resource_energy_resource_id_fkey",
        "power_energy_resource",
        "energy_resource",
        ["energy_resource_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "power_energy_resource_power_id_fkey",
        "power_energy_resource",
        "power",
        ["power_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_constraint(None, "power", type_="foreignkey")
    op.drop_constraint(None, "power", type_="foreignkey")
    op.drop_constraint(None, "power", type_="foreignkey")
    op.drop_constraint(None, "power", type_="foreignkey")
    op.drop_constraint(None, "power", type_="foreignkey")
    op.drop_constraint(None, "power", type_="foreignkey")
    op.drop_constraint(None, "power", type_="foreignkey")
    op.drop_constraint(None, "power", type_="foreignkey")
    op.drop_constraint(None, "power", type_="foreignkey")
    op.create_foreign_key(
        "power_off_taker_id_fkey",
        "power",
        "off_taker",
        ["off_taker_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "power_ppa_status_grid_id_fkey",
        "power",
        "ppa_status",
        ["ppa_status_grid_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "power_technology_id_fkey",
        "power",
        "technology",
        ["technology_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "power_energy_resource_id_fkey",
        "power",
        "energy_resource",
        ["energy_resource_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "power_technology_type_id_fkey",
        "power",
        "technology_type",
        ["technology_type_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "power_unit_id_fkey",
        "power",
        "unit",
        ["unit_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "power_ppa_status_id_fkey",
        "power",
        "ppa_status",
        ["ppa_status_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        "power_capacity_id_fkey",
        "power",
        "capacity",
        ["capacity_id"],
        ["id"],
        onupdate="CASCADE",
        ondelete="CASCADE",
    )
    op.drop_column("power", "other_services")
    op.drop_column("power", "main_service_id")
    # ### end Alembic commands ###