from app.models import (
    Project,
    Power,
)
from app.schemas.power import PowerCreate, PowerUpdate
from app.schemas.project import ProjectCreate, ProjectUpdate

from .base import CRUDBase

power = CRUDBase[Power, PowerCreate, PowerUpdate](Power)
project = CRUDBase[Project, ProjectCreate, ProjectUpdate](Project)
