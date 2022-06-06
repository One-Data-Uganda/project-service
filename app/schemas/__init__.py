from pydantic import BaseModel

from .power import *  # noqa:F401
from .power_impact import *  # noqa:F401
from .power_schedule import *  # noqa:F401
from .project import *  # noqa:F401
from .project_data import *  # noqa:F401
from .project_document import *  # noqa:F401
from .project_investment import *  # noqa:F401
from .project_market import *  # noqa:F401
from .project_team import *  # noqa:F401
from .sponsor import *  # noqa:F401


class FailureResponseModel(BaseModel):
    success: bool
    message: str
