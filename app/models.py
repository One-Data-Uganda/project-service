# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, Text, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship  # noqa:F401
from sqlalchemy_serializer import SerializerMixin

from app.db.base_class import Base

metadata = Base.metadata

class Capacity(Base, SerializerMixin):
    __tablename__ = "capacity"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)


class SponsorType(Base, SerializerMixin):
    __tablename__ = "sponsor_type"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)


class DevelopmentType(Base, SerializerMixin):
    __tablename__ = "development_type"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)


class DevelopmentModel(Base, SerializerMixin):
    __tablename__ = "development_model"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)


class Project(Base, SerializerMixin):
    __tablename__ = "project"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)
    description = Column(Text)
    size = Column(Float)
    investment = Column(Float)
    country_id = Column(Text)
    sector_id = Column(Text)
    segment = Column(Text)
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
        ForeignKey("status.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    sponsor_type_id = Column(
        ForeignKey("sponsor_type.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    reference_code = Column(Text)
    manager = Column(Text)
    development_type_id = Column(
        ForeignKey("development_type.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    development_model_id = Column(
        ForeignKey("development_model.id", ondelete="CASCADE", onupdate="CASCADE")
    )
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


class ProjectRegion(Base, SerializerMixin):
    __tablename__ = "project_region"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(
        ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    region_id = Column(Text)


class ProjectCountry(Base, SerializerMixin):
    __tablename__ = "project_country"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(
        ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    country_id = Column(Text)


class Status(Base, SerializerMixin):
    __tablename__ = "status"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)


class Type(Base, SerializerMixin):
    __tablename__ = "ptype"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)


class ProjectType(Base, SerializerMixin):
    __tablename__ = "project_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(
        ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    type_id = Column(
        ForeignKey("ptype.id", ondelete="CASCADE", onupdate="CASCADE")
    )


class EnergyResource(Base, SerializerMixin):
    __tablename__ = "energy_resource"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)


class HydropowerType(Base, SerializerMixin):
    __tablename__ = "hydropower_type"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)


class Technology(Base, SerializerMixin):
    __tablename__ = "technology"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)


class OffTaker(Base, SerializerMixin):
    __tablename__ = "off_taker"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)


class WaterService(Base, SerializerMixin):
    __tablename__ = "water_service"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)


class PowerWaterService(Base, SerializerMixin):
    __tablename__ = "power_water_service"

    id = Column(Integer, primary_key=True, autoincrement=True)
    power_id = Column(
        ForeignKey("power.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    water_service_id = Column(
        ForeignKey("water_service.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    is_primary = Column(Boolean, server_default=text("false"))


class PowerCustomer(Base, SerializerMixin):
    __tablename__ = "power_customer"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)


class PowerPowerCustomer(Base, SerializerMixin):
    __tablename__ = "power_power_customer"

    id = Column(Integer, primary_key=True, autoincrement=True)
    power_id = Column(
        ForeignKey("power.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    power_customer_id = Column(
        ForeignKey("power_customer.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    is_primary = Column(Boolean, server_default=text("false"))


class PowerEnergyResource(Base, SerializerMixin):
    __tablename__ = "power_energy_resource"

    id = Column(Integer, primary_key=True, autoincrement=True)
    power_id = Column(
        ForeignKey("power.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    energy_resource_id = Column(
        ForeignKey("energy_resource.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    is_primary = Column(Boolean, server_default=text("false"))


class PowerComponent(Base, SerializerMixin):
    __tablename__ = "power_component"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)
    northings = Column(Text)
    eastings = Column(Text)


class PPAstatus(Base, SerializerMixin):
    __tablename__ = "ppa_status"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    name = Column(Text)


class Unit(Base, SerializerMixin):
    __tablename__ = "unit"

    id = Column(Text, primary_key=True)
    name = Column(Text)


class Power(Base, SerializerMixin):
    __tablename__ = "power"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    developer = Column(Text)
    notice = Column(Text)
    picture_source = Column(Text)
    sponsor_id = Column(UUID(as_uuid=True))
    full_name = Column(Text)
    short_name = Column(Text)
    capacity_id = Column(
        ForeignKey("capacity.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    size = Column(Float)
    description = Column(Text)
    sector_id = Column(Text)
    energy_resource_id = Column(
        ForeignKey("energy_resource.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    technology_id = Column(
        ForeignKey("technology.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    hydropower_type_id = Column(
        ForeignKey("hydropower_type.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    other_technologies = Column(Text)
    waterbody_names = Column(Text)
    scheme = Column(Text)
    design_components = Column(Text)
    unit_id = Column(
        ForeignKey("unit.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    average_length = Column(Float)
    average_width = Column(Float)
    off_taker_id = Column(
        ForeignKey("off_taker.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    statutory_permits = Column(Text)
    ppa_status_id = Column(
        ForeignKey("ppa_status.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    ppa_status_grid_id = Column(
        ForeignKey("ppa_status.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    data_shareable_public = Column(Boolean, server_default=text("false"))
    data_shareable_local = Column(Boolean, server_default=text("false"))


class ProjectData(Base, SerializerMixin):
    __tablename__ = "project_data"

    id = Column(UUID(as_uuid=True), primary_key=True)
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
        ForeignKey("capacity.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    turbine_numbers = Column(Integer)
    turbine_capacity = Column(Float)
    turbine_efficiency = Column(Float)
    turbine_capacity_flow = Column(Float)
    alternator_power_output = Column(Float)
    alternator_number = Column(Integer)
    alternator_voltage = Column(Float)
    substation_power_output = Column(Float)
    substation_voltage = Column(Float)




class ProjectDocument(Base, SerializerMixin):
    __tablename__ = "project_document"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    project_id = Column(
        ForeignKey("project.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    document_type = Column(Text)
    name = Column(Text)


class ProjectSponsorType(Base, SerializerMixin):
    __tablename__ = "project_sponsor_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sponsor_id = Column(
        ForeignKey("sponsor.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    sponsor_type_id = Column(
        ForeignKey("sponsor_type.id", ondelete="CASCADE", onupdate="CASCADE")
    )


class SponsorCountry(Base, SerializerMixin):
    __tablename__ = "sponsor_country"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sponsor_id = Column(
        ForeignKey("sponsor.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    country_id = Column(Text)


class SponsorSectorIndustry(Base, SerializerMixin):
    __tablename__ = "sponsor_sector_industry"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sponsor_id = Column(
        ForeignKey("sponsor.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    sector_industry_id = Column(Text)
    is_primary = Column(Boolean, server_default=text("false"))


class SponsorDocument(Base, SerializerMixin):
    __tablename__ = "sponsor_document"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    sponsor_id = Column(
        ForeignKey("sponsor.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    document_type = Column(Text)
    name = Column(Text)


class Sponsor(Base, SerializerMixin):
    __tablename__ = "sponsor"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
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
    required_debt_amount = Column(Text)
    current_lenders = Column(Text)
    prospective_lenders = Column(Text)
    loan_type = Column(Text)
