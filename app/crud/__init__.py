from app.models import (
    Power,
    PowerImpact,
    PowerSchedule,
    Project,
    ProjectData,
    ProjectInvestment,
    ProjectMarket,
    ProjectTeam,
    Sponsor,
)
from app.schemas.power import PowerCreate, PowerUpdate
from app.schemas.power_impact import PowerImpactCreate, PowerImpactUpdate
from app.schemas.power_schedule import PowerScheduleCreate, PowerScheduleUpdate
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.schemas.project_data import ProjectDataCreate, ProjectDataUpdate
from app.schemas.project_investment import (
    ProjectInvestmentCreate,
    ProjectInvestmentUpdate,
)
from app.schemas.project_market import ProjectMarketCreate, ProjectMarketUpdate
from app.schemas.project_team import ProjectTeamCreate, ProjectTeamUpdate
from app.schemas.sponsor import SponsorCreate, SponsorUpdate

from .base import CRUDBase
from .crud_project_document import project_document  # noqa:F401

power = CRUDBase[Power, PowerCreate, PowerUpdate](Power)
project = CRUDBase[Project, ProjectCreate, ProjectUpdate](Project)
power_impact = CRUDBase[PowerImpact, PowerImpactCreate, PowerImpactUpdate](PowerImpact)
power_schedule = CRUDBase[PowerSchedule, PowerScheduleCreate, PowerScheduleUpdate](
    PowerSchedule
)
project_data = CRUDBase[ProjectData, ProjectDataCreate, ProjectDataUpdate](ProjectData)
project_investment = CRUDBase[
    ProjectInvestment, ProjectInvestmentCreate, ProjectInvestmentUpdate
](ProjectInvestment)
project_market = CRUDBase[ProjectMarket, ProjectMarketCreate, ProjectMarketUpdate](
    ProjectMarket
)
project_team = CRUDBase[ProjectTeam, ProjectTeamCreate, ProjectTeamUpdate](ProjectTeam)
sponsor = CRUDBase[Sponsor, SponsorCreate, SponsorUpdate](Sponsor)
