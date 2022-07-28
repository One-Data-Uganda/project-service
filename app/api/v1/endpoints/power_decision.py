import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.PowerDecisionResponse)
async def create_power_decision(
    power_decision_in: schemas.PowerDecisionCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new power_decision.
    """
    try:
        power_decision = crud.power_decision.create(db=db, obj_in=power_decision_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="PowerDecision with this ID already exists"
        )

    return {"success": True, "data": power_decision}


@router.get("/{id}", response_model=schemas.PowerDecisionResponse)
async def get_power_decision(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get power_decision by ID."""
    r = crud.power_decision.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="PowerDecision not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.PowerDecisionResponse)
async def update_power_decision(
    id: uuid.UUID,
    power_decision_in: schemas.PowerDecisionUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a power_decision.
    """
    power_decision = crud.power_decision.get(db=db, id=id)
    if not power_decision:
        raise HTTPException(status_code=404, detail="PowerDecision not found")

    power_decision = crud.power_decision.update(
        db=db, db_obj=power_decision, obj_in=power_decision_in
    )

    return {"success": True, "data": power_decision}


@router.delete("/{id}", response_model=schemas.PowerDecisionResponse)
async def delete_power_decision(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a power_decision.
    """
    power_decision = crud.power_decision.get(db=db, id=id)
    if not power_decision:
        raise HTTPException(status_code=404, detail="PowerDecision not found")

    power_decision = crud.power_decision.remove(db=db, id=id)

    return {"success": True, "data": power_decision}


@router.get("/", response_model=schemas.PowerDecisionListResponse)
async def list_power_decisions(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve power_decisions.
    """
    rows = crud.power_decision.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
