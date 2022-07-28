import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.FinancialPerformanceResponse)
async def create_financial_performance(
    financial_performance_in: schemas.FinancialPerformanceCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new financial_performance.
    """
    try:
        financial_performance = crud.financial_performance.create(
            db=db, obj_in=financial_performance_in
        )
    except Exception:
        raise HTTPException(
            status_code=400, detail="FinancialPerformance with this ID already exists"
        )

    return {"success": True, "data": financial_performance}


@router.get("/{id}", response_model=schemas.FinancialPerformanceResponse)
async def get_financial_performance(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get financial_performance by ID."""
    r = crud.financial_performance.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="FinancialPerformance not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.FinancialPerformanceResponse)
async def update_financial_performance(
    id: uuid.UUID,
    financial_performance_in: schemas.FinancialPerformanceUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a financial_performance.
    """
    financial_performance = crud.financial_performance.get(db=db, id=id)
    if not financial_performance:
        raise HTTPException(status_code=404, detail="FinancialPerformance not found")

    financial_performance = crud.financial_performance.update(
        db=db, db_obj=financial_performance, obj_in=financial_performance_in
    )

    return {"success": True, "data": financial_performance}


@router.delete("/{id}", response_model=schemas.FinancialPerformanceResponse)
async def delete_financial_performance(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a financial_performance.
    """
    financial_performance = crud.financial_performance.get(db=db, id=id)
    if not financial_performance:
        raise HTTPException(status_code=404, detail="FinancialPerformance not found")

    financial_performance = crud.financial_performance.remove(db=db, id=id)

    return {"success": True, "data": financial_performance}


@router.get("/", response_model=schemas.FinancialPerformanceListResponse)
async def list_financial_performances(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve financial_performances.
    """
    rows = crud.financial_performance.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
