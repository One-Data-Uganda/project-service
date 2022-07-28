import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.RiskManagementResponse)
async def create_risk_management(
    risk_management_in: schemas.RiskManagementCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new risk_management.
    """
    try:
        risk_management = crud.risk_management.create(db=db, obj_in=risk_management_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="RiskManagement with this ID already exists"
        )

    return {"success": True, "data": risk_management}


@router.get("/{id}", response_model=schemas.RiskManagementResponse)
async def get_risk_management(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get risk_management by ID."""
    r = crud.risk_management.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="RiskManagement not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.RiskManagementResponse)
async def update_risk_management(
    id: uuid.UUID,
    risk_management_in: schemas.RiskManagementUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a risk_management.
    """
    risk_management = crud.risk_management.get(db=db, id=id)
    if not risk_management:
        raise HTTPException(status_code=404, detail="RiskManagement not found")

    risk_management = crud.risk_management.update(
        db=db, db_obj=risk_management, obj_in=risk_management_in
    )

    return {"success": True, "data": risk_management}


@router.delete("/{id}", response_model=schemas.RiskManagementResponse)
async def delete_risk_management(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a risk_management.
    """
    risk_management = crud.risk_management.get(db=db, id=id)
    if not risk_management:
        raise HTTPException(status_code=404, detail="RiskManagement not found")

    risk_management = crud.risk_management.remove(db=db, id=id)

    return {"success": True, "data": risk_management}


@router.get("/", response_model=schemas.RiskManagementListResponse)
async def list_risk_managements(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve risk_managements.
    """
    rows = crud.risk_management.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
