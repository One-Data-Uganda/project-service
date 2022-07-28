import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.SimpleTableResponse)
async def create_sponsor_document(
    sponsor_document_in: schemas.SimpleTableCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new sponsor_document.
    """
    try:
        sponsor_document = crud.sponsor_document.create(
            db=db, obj_in=sponsor_document_in
        )
    except Exception:
        raise HTTPException(
            status_code=400, detail="SimpleTable with this ID already exists"
        )

    return {"success": True, "data": sponsor_document}


@router.get("/{id}", response_model=schemas.SimpleTableResponse)
async def get_sponsor_document(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get sponsor_document by ID."""
    r = crud.sponsor_document.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.SimpleTableResponse)
async def update_sponsor_document(
    id: uuid.UUID,
    sponsor_document_in: schemas.SimpleTableUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a sponsor_document.
    """
    sponsor_document = crud.sponsor_document.get(db=db, id=id)
    if not sponsor_document:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    sponsor_document = crud.sponsor_document.update(
        db=db, db_obj=sponsor_document, obj_in=sponsor_document_in
    )

    return {"success": True, "data": sponsor_document}


@router.delete("/{id}", response_model=schemas.SimpleTableResponse)
async def delete_sponsor_document(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a sponsor_document.
    """
    sponsor_document = crud.sponsor_document.get(db=db, id=id)
    if not sponsor_document:
        raise HTTPException(status_code=404, detail="SimpleTable not found")

    sponsor_document = crud.sponsor_document.remove(db=db, id=id)

    return {"success": True, "data": sponsor_document}


@router.get("/", response_model=schemas.SimpleTableListResponse)
async def list_sponsor_documents(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve sponsor_documents.
    """
    rows = crud.sponsor_document.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
