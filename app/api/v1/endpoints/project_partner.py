import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.ProjectPartnerResponse)
async def create_project_partner(
    project_partner_in: schemas.ProjectPartnerCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new project_partner.
    """
    try:
        project_partner = crud.project_partner.create(db=db, obj_in=project_partner_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="ProjectPartner with this ID already exists"
        )

    return {"success": True, "data": project_partner}


@router.get("/{id}", response_model=schemas.ProjectPartnerResponse)
async def get_project_partner(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get project_partner by ID."""
    r = crud.project_partner.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="ProjectPartner not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.ProjectPartnerResponse)
async def update_project_partner(
    id: uuid.UUID,
    project_partner_in: schemas.ProjectPartnerUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a project_partner.
    """
    project_partner = crud.project_partner.get(db=db, id=id)
    if not project_partner:
        raise HTTPException(status_code=404, detail="ProjectPartner not found")

    project_partner = crud.project_partner.update(
        db=db, db_obj=project_partner, obj_in=project_partner_in
    )

    return {"success": True, "data": project_partner}


@router.delete("/{id}", response_model=schemas.ProjectPartnerResponse)
async def delete_project_partner(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a project_partner.
    """
    project_partner = crud.project_partner.get(db=db, id=id)
    if not project_partner:
        raise HTTPException(status_code=404, detail="ProjectPartner not found")

    project_partner = crud.project_partner.remove(db=db, id=id)

    return {"success": True, "data": project_partner}


@router.get("/", response_model=schemas.ProjectPartnerListResponse)
async def list_project_partners(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project_partners.
    """
    rows = crud.project_partner.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
