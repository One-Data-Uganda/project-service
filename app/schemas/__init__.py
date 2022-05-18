from pydantic import BaseModel

from .power import *  # noqa
from .project import *  # noqa


class FailureResponseModel(BaseModel):
    success: bool
    message: str
