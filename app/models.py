# coding: utf-8
from sqlalchemy import (
    Boolean,
    Column,
    Date,
    Float,
    ForeignKey,
    Index,
    Integer,
    Text,
    text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship  # noqa:F401
from sqlalchemy_serializer import SerializerMixin

from app.db.base_class import Base

metadata = Base.metadata


class Capacity(Base, SerializerMixin):
    __tablename__ = "capacity"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class SponsorType(Base, SerializerMixin):
    __tablename__ = "sponsor_type"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class DevelopmentType(Base, SerializerMixin):
    __tablename__ = "development_type"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class DevelopmentModel(Base, SerializerMixin):
    __tablename__ = "development_model"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class Project(Base, SerializerMixin):
    __tablename__ = "project"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    account_id = Column(UUID(as_uuid=True))
    featured = Column(Integer, server_default=text("0"))
    type = Column(Text)
    name = Column(Text)
    short_name = Column(Text)
    brief_description = Column(Text)
    description = Column(Text)
    size = Column(Float)
    investment = Column(Float)
    country_id = Column(Text)
    sector_industry_id = Column(Text)
    sector_group_id = Column(Text)
    sector_division_id = Column(Text)
    sector_id = Column(Text)
    technology = Column(Text)
    status = Column(Text)
    commencement_date = Column(Date)
    proposed_completion_date = Column(Date)
    current_stage = Column(Text)
    next_stages = Column(Text)
    estimated_cost = Column(Float)
    contact_information = Column(Text)
    contact_address = Column(Text)
    postal_address = Column(Text)
    telephone = Column(Text)
    email = Column(Text)
    website = Column(Text)
    completed_activities = Column(Text)
    current_activities = Column(Text)
    next_activities = Column(Text)
    outstanding_activities = Column(Text)
    status_id = Column(
        ForeignKey("status.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    sponsor_type_id = Column(
        ForeignKey("sponsor_type.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    reference_code = Column(Text)
    manager = Column(Text)
    development_type_id = Column(
        ForeignKey("development_type.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    development_model = Column(Text)
    percentage_public = Column(Float)
    percentage_private = Column(Float)
    location = Column(Text)
    nearest_town = Column(Text)
    distance = Column(Float)
    nearest_capital_country_id = Column(Text)
    nearest_capital = Column(Text)
    distance_capital = Column(Float)
    environmental_impact = Column(Text)
    social_impact = Column(Text)
    total_investment = Column(Float)
    equity_investment = Column(Float)
    debt_amount = Column(Float)
    grant_amount = Column(Float)
    outstanding_investment = Column(Float)
    related_projects = Column(Text)
    strategy = Column(Text)
    alliances = Column(Text)
    objectives = Column(Text)
    location_area = Column(Text)
    milestones = Column(Text)
    impacts = Column(Text)
    related_projects = Column(Text)
    award_criteria = Column(Text)
    comparative_advantage = Column(Text)
    economic_contributions = Column(Text)
    image_stamp = Column(Float)


class ProjectRegion(Base, SerializerMixin):
    __tablename__ = "project_region"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(
        ForeignKey("project.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    region_id = Column(Text)


class ProjectCountry(Base, SerializerMixin):
    __tablename__ = "project_country"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(
        ForeignKey("project.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    country_id = Column(Text)


class Status(Base, SerializerMixin):
    __tablename__ = "status"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class Type(Base, SerializerMixin):
    __tablename__ = "ptype"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class ProjectType(Base, SerializerMixin):
    __tablename__ = "project_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(
        ForeignKey("project.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    type_id = Column(ForeignKey("ptype.id", ondelete="RESTRICT", onupdate="RESTRICT"))


class EnergyResource(Base, SerializerMixin):
    __tablename__ = "energy_resource"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class TechnologyType(Base, SerializerMixin):
    __tablename__ = "technology_type"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    technology_id = Column(
        ForeignKey("technology.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    name = Column(Text)

    technology = relationship("Technology")


class Technology(Base, SerializerMixin):
    __tablename__ = "technology"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class OffTaker(Base, SerializerMixin):
    __tablename__ = "off_taker"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class WaterService(Base, SerializerMixin):
    __tablename__ = "water_service"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class PowerWaterService(Base, SerializerMixin):
    __tablename__ = "power_water_service"

    id = Column(Integer, primary_key=True, autoincrement=True)
    power_id = Column(ForeignKey("power.id", ondelete="RESTRICT", onupdate="RESTRICT"))
    water_service_id = Column(
        ForeignKey("water_service.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    is_primary = Column(Boolean, server_default=text("false"))


class PowerCustomer(Base, SerializerMixin):
    __tablename__ = "power_customer"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class PowerPowerCustomer(Base, SerializerMixin):
    __tablename__ = "power_power_customer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    power_id = Column(ForeignKey("power.id", ondelete="RESTRICT", onupdate="RESTRICT"))
    power_customer_id = Column(
        ForeignKey("power_customer.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    is_primary = Column(Boolean, server_default=text("false"))


class PowerEnergyResource(Base, SerializerMixin):
    __tablename__ = "power_energy_resource"

    id = Column(Integer, primary_key=True, autoincrement=True)
    power_id = Column(ForeignKey("power.id", ondelete="RESTRICT", onupdate="RESTRICT"))
    energy_resource_id = Column(
        ForeignKey("energy_resource.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    is_primary = Column(Boolean, server_default=text("false"))


class PowerComponent(Base, SerializerMixin):
    __tablename__ = "power_component"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)
    northings = Column(Text)
    eastings = Column(Text)


class PPAstatus(Base, SerializerMixin):
    __tablename__ = "ppa_status"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class Unit(Base, SerializerMixin):
    __tablename__ = "unit"

    id = Column(Text, primary_key=True)
    name = Column(Text)


class Power(Base, SerializerMixin):
    __tablename__ = "power"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    developer = Column(Text)
    notice = Column(Text)
    picture_source = Column(Text)
    sponsor_id = Column(UUID(as_uuid=True))
    sponsor_name = Column(Text)
    capacity_id = Column(
        ForeignKey("capacity.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    size = Column(Float)
    energy_resource_id = Column(
        ForeignKey("energy_resource.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    technology_id = Column(
        ForeignKey("technology.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    technology_type_id = Column(
        ForeignKey("technology_type.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    other_technologies = Column(Text)
    waterbody_names = Column(Text)
    scheme = Column(Text)
    design_components = Column(Text)
    unit_id = Column(ForeignKey("unit.id", ondelete="RESTRICT", onupdate="RESTRICT"))
    northings = Column(Text)
    eastings = Column(Text)
    average_length = Column(Float)
    average_width = Column(Float)
    data_shareable_public = Column(Boolean, server_default=text("false"))
    data_shareable_local = Column(Boolean, server_default=text("false"))
    main_service_id = Column(
        ForeignKey("water_service.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    other_service_ids = Column(Text)
    other_services = Column(Text)
    off_taker_id = Column(
        ForeignKey("off_taker.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    statutory_permits = Column(Text)
    statutory_licences = Column(Text)
    statutory_agreements = Column(Text)
    power_customer_id = Column(
        ForeignKey("power_customer.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    other_customer_ids = Column(Text)
    other_customers = Column(Text)
    revenue_source_id = Column(
        ForeignKey("water_service.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    ppa_status_id = Column(
        ForeignKey("ppa_status.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    ppa_status_grid_id = Column(
        ForeignKey("ppa_status.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    ppa_period = Column(Integer)
    outstanding_activities = Column(Text)
    environmental_impacts = Column(Text)
    related_projects = Column(Text)


class PowerDecision(Base, SerializerMixin):
    __tablename__ = "power_decision"

    id = Column(UUID(as_uuid=True), primary_key=True)
    commencement_date = Column(Date)
    client_approval_date = Column(Date)
    planning_date = Column(Date)
    equity_finance_date = Column(Date)
    debt_finance_date = Column(Date)
    technical_assistance_date = Column(Date)
    financial_close_date = Column(Date)
    construction_start_date = Column(Date)
    commissioning_date = Column(Date)
    commercial_operations_date = Column(Date)


class ProjectData(Base, SerializerMixin):
    __tablename__ = "project_data"

    id = Column(UUID(as_uuid=True), primary_key=True)
    weir_classification = Column(Text)
    height = Column(Text)
    size_class = Column(Text)
    hazard_potential = Column(Text)
    type_of_dam = Column(Text)
    dam_length = Column(Float)
    crest_width = Column(Float)
    catchment_area = Column(Float)
    design_flow = Column(Float)
    maximum_flood = Column(Float)
    q100 = Column(Float)
    q200 = Column(Float)
    canal_length = Column(Float)
    canal_width = Column(Float)
    canal_velocity = Column(Float)
    spillway_type = Column(Text)
    spillway_length = Column(Float)
    spillway_free_board = Column(Float)
    spillway_discharge_capacity = Column(Float)
    penstocks_type = Column(Text)
    penstocks_length = Column(Float)
    penstocks_diameter = Column(Float)
    penstocks_velocity = Column(Float)
    penstocks_thickness = Column(Float)
    penstocks_number = Column(Float)
    installation_method = Column(Text)
    upstream_control = Column(Text)
    inlet_control = Column(Text)
    outlet_control = Column(Text)
    overhead_crane = Column(Float)
    turbine_type = Column(Text)
    turbine_capacity_id = Column(
        ForeignKey("capacity.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    turbine_unit_size = Column(Float)
    turbine_numbers = Column(Integer)
    turbine_capacity = Column(Float)
    turbine_efficiency = Column(Float)
    turbine_capacity_flow = Column(Float)
    alternator_power_output = Column(Float)
    alternator_number = Column(Integer)
    alternator_voltage = Column(Float)
    substation_power_output = Column(Float)
    substation_voltage = Column(Float)
    share_data_public = Column(Boolean)
    share_data = Column(Boolean)


class ProjectDocument(Base, SerializerMixin):
    __tablename__ = "project_document"
    __table_args__ = (
        Index(
            "project_document_unique",
            "project_id",
            "name",
            "document_type",
            unique=True,
        ),
    )

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    project_id = Column(
        ForeignKey("project.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    section = Column(Text)
    document_type = Column(Text)
    name = Column(Text)
    mimetype = Column(Text)
    size = Column(Integer)


class ProjectSponsorType(Base, SerializerMixin):
    __tablename__ = "project_sponsor_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sponsor_id = Column(
        ForeignKey("sponsor.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    sponsor_type_id = Column(
        ForeignKey("sponsor_type.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )


class SponsorCountry(Base, SerializerMixin):
    __tablename__ = "sponsor_country"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sponsor_id = Column(
        ForeignKey("sponsor.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    country_id = Column(Text)


class SponsorSectorIndustry(Base, SerializerMixin):
    __tablename__ = "sponsor_sector_industry"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sponsor_id = Column(
        ForeignKey("sponsor.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    sector_industry_id = Column(Text)
    is_primary = Column(Boolean, server_default=text("false"))


class SponsorDocument(Base, SerializerMixin):
    __tablename__ = "sponsor_document"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    sponsor_id = Column(
        ForeignKey("sponsor.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    document_type = Column(Text)
    name = Column(Text)


class Sponsor(Base, SerializerMixin):
    __tablename__ = "sponsor"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(Text)
    other_sponsors = Column(Text)
    shareholders = Column(Text)
    background = Column(Text)
    experience = Column(Text)
    ownership = Column(Text)
    percentage_public = Column(Float)
    percentage_private = Column(Float)
    percentage_academic = Column(Float)
    products = Column(Text)
    other_projects = Column(Text)
    compliance = Column(Text)
    partners = Column(Text)
    capital_statement = Column(Text)
    contact_person = Column(Text)
    contact_address = Column(Text)
    contact_postal = Column(Text)
    contact_email = Column(Text)
    contact_telephone = Column(Text)
    contact_website = Column(Text)
    sponsor_types = Column(Text)
    countries = Column(Text)
    other_countries = Column(Text)
    sector_industry_id = Column(Text)
    other_sectors = Column(Text)


class ProjectTeam(Base, SerializerMixin):
    __tablename__ = "project_team"

    id = Column(UUID(as_uuid=True), primary_key=True)
    manager = Column(Text)
    manager_background = Column(Text)
    has_board = Column(Boolean, server_default=text("false"))
    number_directors = Column(Integer)
    board_directors = Column(Text)
    management_oficers = Column(Text)
    technical_staff = Column(Text)
    management_targets = Column(Text)
    management_agreement = Column(Text)
    personnel_practices = Column(Text)
    manager_nin = Column(Text)
    nin_validate = Column(Boolean, server_default=text("false"))


class PowerSchedule(Base, SerializerMixin):
    __tablename__ = "power_schedule"

    id = Column(UUID(as_uuid=True), primary_key=True)
    construction_schedule = Column(Text)
    startup_schedule = Column(Text)
    operations_schedule = Column(Text)
    expenditures = Column(Text)
    funding_schedule = Column(Text)
    regulatory_compliance = Column(Text)


class PowerImpact(Base, SerializerMixin):
    __tablename__ = "power_impact"

    id = Column(UUID(as_uuid=True), primary_key=True)
    description_environment = Column(Text)
    description_social = Column(Text)
    description_environment_impact = Column(Text)
    description_social_impact = Column(Text)
    treatment_plans = Column(Text)
    occupational_hazards = Column(Text)
    local_regulations = Column(Text)
    sponsor_contribution = Column(Text)
    key_partners = Column(Text)
    environmental_concerns = Column(Text)
    esmp = Column(Text)


class ProjectMarket(Base, SerializerMixin):
    __tablename__ = "project_market"

    id = Column(UUID(as_uuid=True), primary_key=True)
    overview = Column(Text)
    economic_issues = Column(Text)
    energy_sector = Column(Text)
    electricity_sector = Column(Text)
    sector_policies = Column(Text)
    laws = Column(Text)
    key_stakeholders = Column(Text)
    outlook = Column(Text)
    competition = Column(Text)
    main_competitors = Column(Text)
    competitive_advantage = Column(Text)
    strengths = Column(Text)
    weaknesses = Column(Text)
    opportunities = Column(Text)
    threats = Column(Text)


class ProjectInvestment(Base, SerializerMixin):
    __tablename__ = "project_investment"

    id = Column(UUID(as_uuid=True), primary_key=True)
    total_cost = Column(Float)
    required_investment = Column(Text)
    shareholder_structure = Column(Text)
    equity_investors = Column(Text)
    equity_partners = Column(Text)
    prospective_equity_amount = Column(Float)
    required_equity_amount = Column(Float)
    equity_mobilized = Column(Float)
    equity_needed = Column(Float)
    required_debt_amount = Column(Float)
    current_lenders = Column(Text)
    prospective_lenders = Column(Text)
    loan_type = Column(Text)
    other_loan_types = Column(Text)
    other_loan_description = Column(Text)
    loan_amount = Column(Float)
    loan_mobilized = Column(Float)
    loan_needing_mobilization = Column(Float)
    proposed_grant_amount = Column(Text)
    grant_providers = Column(Text)
    prospective_grant_providers = Column(Text)
    grant_types = Column(Text)
    grant_amount = Column(Float)
    grant_mobilized = Column(Float)
    grant_needing_mobilization = Column(Float)
    total_mobilized = Column(Float)
    total_needing_mobilization = Column(Float)


class ProjectPartner(Base, SerializerMixin):
    __tablename__ = "project_partner"

    id = Column(UUID(as_uuid=True), primary_key=True)
    equity_partners = Column(Text)
    debt_partners = Column(Text)
    tehcnical_advisors = Column(Text)
    implementation_partners = Column(Text)
    institutional_partners = Column(Text)
    stakeholders = Column(Text)


class ProjectLegal(Base, SerializerMixin):
    __tablename__ = "project_legal"

    id = Column(UUID(as_uuid=True), primary_key=True)
    sponsor_status = Column(Text)
    permits_status = Column(Text)
    licenses_status = Column(Text)
    statutory_status = Column(Text)
    jv_status = Column(Text)
    sector_policies = Column(Text)
    sector_laws = Column(Text)


class ProductService(Base, SerializerMixin):
    __tablename__ = "product_service"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class ProductCustomer(Base, SerializerMixin):
    __tablename__ = "product_customer"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    name = Column(Text)


class PowerProduct(Base, SerializerMixin):
    __tablename__ = "power_product"

    id = Column(UUID(as_uuid=True), primary_key=True)
    product_service_id = Column(
        ForeignKey("product_service.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    other_services = Column(Text)
    product_unit_id = Column(Text)
    annual_output = Column(Float)
    annual_demand = Column(Float)
    primary_customer_id = Column(
        ForeignKey("power_customer.id", ondelete="RESTRICT", onupdate="RESTRICT")
    )
    other_customers = Column(Text)
    other_customer_desc = Column(Text)

    product_service = relationship("ProductService")
    primary_customer = relationship("PowerCustomer")


class FinancialPerformance(Base, SerializerMixin):
    __tablename__ = "financial_performance"

    id = Column(UUID(as_uuid=True), primary_key=True)
    main_revenue_sources = Column(Text)
    other_revenue_sources = Column(Text)
    ppa_period = Column(Integer)
    average_annual_output = Column(Float)
    tariff_price = Column(Float)
    average_annual_revenue = Column(Float)
    total_revenue = Column(Float)
    capital_investment = Column(Float)
    capital_cost_percentage = Column(Float)
    payback_period = Column(Integer)
    npv = Column(Float)
    average_annual_costs = Column(Float)
    average_annual_expenses = Column(Float)
    total_annual_costs = Column(Float)
    applicable_cost_period = Column(Integer)
    total_costs_period = Column(Integer)
    total_net_revenue = Column(Float)
    average_annual_net_revenue = Column(Float)
    key_model_results = Column(Text)


class RiskManagement(Base, SerializerMixin):
    __tablename__ = "risk_management"

    id = Column(UUID(as_uuid=True), primary_key=True)
    summary = Column(Text)
    current_partners = Column(Text)
    prospective_partners = Column(Text)
    product_types = Column(Text)
    budget_amount = Column(Float)
    budget_amount_mobilized = Column(Float)
    budget_amount_needed = Column(Float)
    amount = Column(Float)
    guarantees = Column(Text)
    guarantee_types = Column(Text)
    current_guarantee_issuance = Column(Text)
    prospective_guarantee_issuance = Column(Text)
    required_guarantee_amount = Column(Float)
    outstanding_guarantee_amount = Column(Float)
    guarantees_documentation = Column(Text)
    government_support = Column(Text)
    direct_government_support = Column(Text)
    direct_government_value = Column(Float)
    indirect_government_support = Column(Text)
    indirect_government_value = Column(Float)


class ProjectContact(Base, SerializerMixin):
    __tablename__ = "project_contact"

    id = Column(UUID(as_uuid=True), primary_key=True)
    project_contact = Column(Text)
    project_address = Column(Text)
    project_postal = Column(Text)
    project_email = Column(Text)
    project_telephone = Column(Text)
    project_website = Column(Text)
    project_nin = Column(Text)
    project_nin_validate = Column(Boolean, server_default=text("false"))
    general_contact = Column(Text)
    general_address = Column(Text)
    general_postal = Column(Text)
    general_email = Column(Text)
    general_telephone = Column(Text)
    general_website = Column(Text)
    general_nin = Column(Text)
    general_nin_validate = Column(Boolean, server_default=text("false"))
