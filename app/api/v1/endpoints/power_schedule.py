from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.PowerScheduleResponse)
async def create_power_schedule(
    power_schedule_in: schemas.PowerScheduleCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new power_schedule.
    """
    try:
        power_schedule = crud.power_schedule.create(db=db, obj_in=power_schedule_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="Power Schedule with this ID already exists"
        )

    return {"success": True, "data": power_schedule}


@router.get("/{id}", response_model=schemas.PowerScheduleResponse)
async def get_power_schedule(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get power schedule by ID."""
    r = crud.power_schedule.get(db, id)
    if not r:
        raise HTTPException(status_code=401, detail="Power Schedule not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.PowerScheduleResponse)
async def update_power_schedule(
    id: str,
    power_schedule_in: schemas.PowerScheduleUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a power schedule.
    """
    power_schedule = crud.power_schedule.get(db=db, id=id)
    if not power_schedule:
        raise HTTPException(status_code=404, detail="Power Schedule not found")

    power_schedule = crud.power_schedule.update(
        db=db, db_obj=power_schedule, obj_in=power_schedule_in
    )

    return {"success": True, "data": power_schedule}


@router.delete("/{id}", response_model=schemas.PowerScheduleResponse)
async def delete_power_schedule(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a power schedule.
    """
    power_schedule = crud.power_schedule.get(db=db, id=id)
    if not power_schedule:
        raise HTTPException(status_code=404, detail="Power Schedule not found")

    power_schedule = crud.power_schedule.remove(db=db, id=id)

    return {"success": True, "data": power_schedule}


@router.get("/", response_model=schemas.PowerScheduleListResponse)
async def list_power_schedules(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve power schedules.
    """
    rows = crud.power_schedule.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
