import uuid
from typing import List, Optional

from pydantic import BaseModel

from .capacity import Capacity


# Shared properties
class ProjectDataBase(BaseModel):
    id: Optional[uuid.UUID]
    who: Optional[str]
    weir_classification: Optional[str]
    height: Optional[str]
    size_class: Optional[str]
    hazard_potential: Optional[str]
    type_of_dam: Optional[str]
    dam_length: Optional[float]
    crest_width: Optional[float]
    catchment_area: Optional[float]
    design_flow: Optional[float]
    maximum_flood: Optional[float]
    q100: Optional[float]
    q200: Optional[float]
    canal_length: Optional[float]
    canal_width: Optional[float]
    canal_velocity: Optional[float]
    spillway_type: Optional[str]
    spillway_length: Optional[float]
    spillway_free_board: Optional[float]
    spillway_discharge_capacity: Optional[float]
    forebay_capacity: Optional[float]
    forebay_length: Optional[float]
    forebay_width: Optional[float]
    forebay_depth: Optional[float]
    penstocks_type: Optional[str]
    penstocks_length: Optional[float]
    penstocks_diameter: Optional[float]
    penstocks_velocity: Optional[float]
    penstocks_thickness: Optional[float]
    penstocks_number: Optional[float]
    installation_method: Optional[str]
    power_house_floor: Optional[float]
    upstream_control: Optional[str]
    inlet_control: Optional[str]
    outlet_control: Optional[str]
    overhead_crane: Optional[float]
    turbine_type: Optional[str]
    turbine_capacity_id: Optional[str]
    turbine_unit_size: Optional[float]
    turbine_numbers: Optional[int]
    turbine_capacity: Optional[float]
    turbine_efficiency: Optional[float]
    turbine_capacity_flow: Optional[float]
    alternator_power_output: Optional[float]
    alternator_number: Optional[int]
    alternator_voltage: Optional[float]
    tail_type: Optional[str]
    tail_length: Optional[float]
    tail_width: Optional[float]
    substation_power_output: Optional[float]
    substation_voltage: Optional[float]
    share_data_public: Optional[bool]
    share_data: Optional[bool]
    head_gross: Optional[float]
    head_net: Optional[float]
    head_classification: Optional[str]


# Properties to receive via API on creation
class ProjectDataCreate(ProjectDataBase):
    pass


class ProjectDataUpdate(ProjectDataBase):
    pass


class ProjectDataInDBBase(ProjectDataBase):
    turbine_cap: Optional[Capacity]

    class Config:
        orm_mode = True


# Additional properties to return via API
class ProjectData(ProjectDataInDBBase):
    pass


# Additional properties stored in DB
class ProjectDataInDB(ProjectDataInDBBase):
    pass


class ProjectDataResponse(BaseModel):
    success: bool
    data: ProjectData


class ProjectDataListResponse(BaseModel):
    success: bool
    data: Optional[List[ProjectData]]
