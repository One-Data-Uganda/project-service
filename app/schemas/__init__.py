from pydantic import BaseModel

from .capacity import *  # noqa
from .financial_performance import *  # noqa
from .power import *  # noqa
from .power_decision import *  # noqa
from .power_impact import *  # noqa
from .power_product import *  # noqa
from .power_schedule import *  # noqa
from .project import *  # noqa
from .project_contact import *  # noqa
from .project_data import *  # noqa
from .project_document import *  # noqa
from .project_investment import *  # noqa
from .project_legal import *  # noqa
from .project_market import *  # noqa
from .project_partner import *  # noqa
from .project_status import *  # noqa
from .project_team import *  # noqa
from .risk_management import *  # noqa
from .simple_table import *  # noqa
from .sponsor import *  # noqa


class FailureResponseModel(BaseModel):
    success: bool
    message: str
