import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.ProjectMarketResponse)
async def create_project_market(
    project_market_in: schemas.ProjectMarketCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new project_market.
    """
    try:
        project_market = crud.project_market.create(db=db, obj_in=project_market_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="ProjectMarket with this ID already exists"
        )

    return {"success": True, "data": project_market}


@router.get("/{id}", response_model=schemas.ProjectMarketResponse)
async def get_project_market(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get project_market by ID."""
    r = crud.project_market.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="ProjectMarket not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.ProjectMarketResponse)
async def update_project_market(
    id: uuid.UUID,
    project_market_in: schemas.ProjectMarketUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a project_market.
    """
    project_market = crud.project_market.get(db=db, id=id)
    if not project_market:
        raise HTTPException(status_code=404, detail="ProjectMarket not found")

    project_market = crud.project_market.update(
        db=db, db_obj=project_market, obj_in=project_market_in
    )

    return {"success": True, "data": project_market}


@router.delete("/{id}", response_model=schemas.ProjectMarketResponse)
async def delete_project_market(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a project_market.
    """
    project_market = crud.project_market.get(db=db, id=id)
    if not project_market:
        raise HTTPException(status_code=404, detail="ProjectMarket not found")

    project_market = crud.project_market.remove(db=db, id=id)

    return {"success": True, "data": project_market}


@router.get("/", response_model=schemas.ProjectMarketListResponse)
async def list_project_markets(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project_markets.
    """
    rows = crud.project_market.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
