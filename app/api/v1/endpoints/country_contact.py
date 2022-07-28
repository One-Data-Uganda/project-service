from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.PowerImpactResponse)
async def create_power_impact(
    power_impact_in: schemas.PowerImpactCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new power_impact.
    """
    try:
        power_impact = crud.power_impact.create(db=db, obj_in=power_impact_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="Power Impact with this ID already exists"
        )

    return power_impact


@router.get("/{id}", response_model=schemas.PowerImpactResponse)
async def get_power_impact(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get power impact by ID."""
    r = crud.power_impact.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="Power Impact not found")

    return r


@router.put("/{id}", response_model=schemas.PowerImpactResponse)
async def update_power_impact(
    id: str,
    power_impact_in: schemas.PowerImpactUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a power impact.
    """
    power_impact = crud.power_impact.get(db=db, id=id)
    if not power_impact:
        raise HTTPException(status_code=404, detail="Power Impact not found")

    power_impact = crud.power_impact.update(
        db=db, db_obj=power_impact, obj_in=power_impact_in
    )

    return power_impact


@router.delete("/{id}", response_model=schemas.PowerImpactResponse)
async def delete_power_impact(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a power impact.
    """
    power_impact = crud.power_impact.get(db=db, id=id)
    if not power_impact:
        raise HTTPException(status_code=404, detail="Power Impact not found")

    power_impact = crud.power_impact.remove(db=db, id=id)

    return power_impact


@router.get("/", response_model=schemas.PowerImpactListResponse)
async def list_power_impacts(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve power impacts.
    """
    rows = crud.power_impact.get_multi(db, limit=1000)

    return rows
