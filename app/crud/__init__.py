from app.models import (
    Capacity,
    DevelopmentModel,
    DevelopmentType,
    EnergyResource,
    FinancialPerformance,
    OffTaker,
    Power,
    PowerComponent,
    PowerCustomer,
    PowerDecision,
    PowerEnergyResource,
    PowerImpact,
    PowerPowerCustomer,
    PowerProduct,
    PowerSchedule,
    PowerWaterService,
    PPAStatus,
    ProductCustomer,
    ProductService,
    ProjectContact,
    ProjectCountry,
    ProjectData,
    ProjectInvestment,
    ProjectLegal,
    ProjectMarket,
    ProjectPartner,
    ProjectRegion,
    ProjectSponsorType,
    ProjectTeam,
    ProjectType,
    RiskManagement,
    Sponsor,
    SponsorCountry,
    SponsorDocument,
    SponsorSectorIndustry,
    SponsorType,
    Status,
    Technology,
    TechnologyType,
    Unit,
    WaterService,
)
from app.schemas.capacity import CapacityCreate, CapacityUpdate
from app.schemas.financial_performance import (
    FinancialPerformanceCreate,
    FinancialPerformanceUpdate,
)
from app.schemas.power import PowerCreate, PowerUpdate
from app.schemas.power_decision import PowerDecisionCreate, PowerDecisionUpdate
from app.schemas.power_impact import PowerImpactCreate, PowerImpactUpdate
from app.schemas.power_product import PowerProductCreate, PowerProductUpdate
from app.schemas.power_schedule import PowerScheduleCreate, PowerScheduleUpdate
from app.schemas.project_contact import ProjectContactCreate, ProjectContactUpdate
from app.schemas.project_data import ProjectDataCreate, ProjectDataUpdate
from app.schemas.project_investment import (
    ProjectInvestmentCreate,
    ProjectInvestmentUpdate,
)
from app.schemas.project_legal import ProjectLegalCreate, ProjectLegalUpdate
from app.schemas.project_market import ProjectMarketCreate, ProjectMarketUpdate
from app.schemas.project_partner import ProjectPartnerCreate, ProjectPartnerUpdate
from app.schemas.project_team import ProjectTeamCreate, ProjectTeamUpdate
from app.schemas.risk_management import RiskManagementCreate, RiskManagementUpdate
from app.schemas.simple_table import SimpleTableCreate, SimpleTableUpdate
from app.schemas.sponsor import SponsorCreate, SponsorUpdate

from .base import CRUDBase
from .crud_project import project  # noqa
from .crud_project_document import project_document  # noqa

capacity = CRUDBase[Capacity, CapacityCreate, CapacityUpdate](Capacity)
development_model = CRUDBase[DevelopmentModel, SimpleTableCreate, SimpleTableUpdate](
    DevelopmentModel
)
development_type = CRUDBase[DevelopmentType, SimpleTableCreate, SimpleTableUpdate](
    DevelopmentType
)
energy_resource = CRUDBase[EnergyResource, SimpleTableCreate, SimpleTableUpdate](
    EnergyResource
)
financial_performance = CRUDBase[
    FinancialPerformance, FinancialPerformanceCreate, FinancialPerformanceUpdate
](FinancialPerformance)
off_taker = CRUDBase[OffTaker, SimpleTableCreate, SimpleTableUpdate](OffTaker)
power = CRUDBase[Power, PowerCreate, PowerUpdate](Power)
power_component = CRUDBase[PowerComponent, SimpleTableCreate, SimpleTableUpdate](
    PowerComponent
)
power_customer = CRUDBase[PowerCustomer, SimpleTableCreate, SimpleTableUpdate](
    PowerCustomer
)
power_decision = CRUDBase[PowerDecision, PowerDecisionCreate, PowerDecisionUpdate](
    PowerDecision
)
power_energy_resource = CRUDBase[
    PowerEnergyResource, SimpleTableCreate, SimpleTableUpdate
](PowerEnergyResource)
power_impact = CRUDBase[PowerImpact, PowerImpactCreate, PowerImpactUpdate](PowerImpact)
power_power_customer = CRUDBase[
    PowerPowerCustomer, SimpleTableCreate, SimpleTableUpdate
](PowerPowerCustomer)
power_product = CRUDBase[PowerProduct, PowerProductCreate, PowerProductUpdate](
    PowerProduct
)
power_schedule = CRUDBase[PowerSchedule, PowerScheduleCreate, PowerScheduleUpdate](
    PowerSchedule
)
power_water_service = CRUDBase[PowerWaterService, SimpleTableCreate, SimpleTableUpdate](
    PowerWaterService
)
ppa_status = CRUDBase[PPAStatus, SimpleTableCreate, SimpleTableUpdate](PPAStatus)
product_customer = CRUDBase[ProductCustomer, SimpleTableCreate, SimpleTableUpdate](
    ProductCustomer
)
product_service = CRUDBase[ProductService, SimpleTableCreate, SimpleTableUpdate](
    ProductService
)
project_contact = CRUDBase[ProjectContact, ProjectContactCreate, ProjectContactUpdate](
    ProjectContact
)
project_country = CRUDBase[ProjectCountry, SimpleTableCreate, SimpleTableUpdate](
    ProjectCountry
)
project_data = CRUDBase[ProjectData, ProjectDataCreate, ProjectDataUpdate](ProjectData)
project_investment = CRUDBase[
    ProjectInvestment, ProjectInvestmentCreate, ProjectInvestmentUpdate
](ProjectInvestment)
project_legal = CRUDBase[ProjectLegal, ProjectLegalCreate, ProjectLegalUpdate](
    ProjectLegal
)
project_market = CRUDBase[ProjectMarket, ProjectMarketCreate, ProjectMarketUpdate](
    ProjectMarket
)
project_partner = CRUDBase[ProjectPartner, ProjectPartnerCreate, ProjectPartnerUpdate](
    ProjectPartner
)
project_region = CRUDBase[ProjectRegion, SimpleTableCreate, SimpleTableUpdate](
    ProjectRegion
)
project_sponsor_type = CRUDBase[
    ProjectSponsorType, SimpleTableCreate, SimpleTableUpdate
](ProjectSponsorType)
project_team = CRUDBase[ProjectTeam, ProjectTeamCreate, ProjectTeamUpdate](ProjectTeam)
project_type = CRUDBase[ProjectType, SimpleTableCreate, SimpleTableUpdate](ProjectType)
risk_management = CRUDBase[RiskManagement, RiskManagementCreate, RiskManagementUpdate](
    RiskManagement
)
sponsor = CRUDBase[Sponsor, SponsorCreate, SponsorUpdate](Sponsor)
sponsor_country = CRUDBase[SponsorCountry, SimpleTableCreate, SimpleTableUpdate](
    SponsorCountry
)
sponsor_document = CRUDBase[SponsorDocument, SimpleTableCreate, SimpleTableUpdate](
    SponsorDocument
)
sponsor_sector_industry = CRUDBase[
    SponsorSectorIndustry, SimpleTableCreate, SimpleTableUpdate
](SponsorSectorIndustry)
sponsor_type = CRUDBase[SponsorType, SimpleTableCreate, SimpleTableUpdate](SponsorType)
status = CRUDBase[Status, SimpleTableCreate, SimpleTableUpdate](Status)
technology = CRUDBase[Technology, SimpleTableCreate, SimpleTableUpdate](Technology)
technology_type = CRUDBase[TechnologyType, SimpleTableCreate, SimpleTableUpdate](
    TechnologyType
)
unit = CRUDBase[Unit, SimpleTableCreate, SimpleTableUpdate](Unit)
water_service = CRUDBase[WaterService, SimpleTableCreate, SimpleTableUpdate](
    WaterService
)
