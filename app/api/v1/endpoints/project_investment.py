import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.ProjectInvestmentResponse)
async def create_project_investment(
    project_investment_in: schemas.ProjectInvestmentCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new project_investment.
    """
    try:
        project_investment = crud.project_investment.create(
            db=db, obj_in=project_investment_in
        )
    except Exception:
        raise HTTPException(
            status_code=400, detail="ProjectInvestment with this ID already exists"
        )

    return {"success": True, "data": project_investment}


@router.get("/{id}", response_model=schemas.ProjectInvestmentResponse)
async def get_project_investment(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get project_investment by ID."""
    r = crud.project_investment.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="ProjectInvestment not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.ProjectInvestmentResponse)
async def update_project_investment(
    id: uuid.UUID,
    project_investment_in: schemas.ProjectInvestmentUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a project_investment.
    """
    project_investment = crud.project_investment.get(db=db, id=id)
    if not project_investment:
        raise HTTPException(status_code=404, detail="ProjectInvestment not found")

    project_investment = crud.project_investment.update(
        db=db, db_obj=project_investment, obj_in=project_investment_in
    )

    return {"success": True, "data": project_investment}


@router.delete("/{id}", response_model=schemas.ProjectInvestmentResponse)
async def delete_project_investment(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a project_investment.
    """
    project_investment = crud.project_investment.get(db=db, id=id)
    if not project_investment:
        raise HTTPException(status_code=404, detail="ProjectInvestment not found")

    project_investment = crud.project_investment.remove(db=db, id=id)

    return {"success": True, "data": project_investment}


@router.get("/", response_model=schemas.ProjectInvestmentListResponse)
async def list_project_investments(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project_investments.
    """
    rows = crud.project_investment.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
