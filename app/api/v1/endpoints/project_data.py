import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.logger import TimedRoute, log  # noqa

router = APIRouter(route_class=TimedRoute)


@router.post("/", response_model=schemas.ProjectDataResponse)
async def create_project_data(
    project_data_in: schemas.ProjectDataCreate,
    db: Session = Depends(deps.get_db),
) -> Any:

    """
    Create new project_data.
    """
    try:
        project_data = crud.project_data.create(db=db, obj_in=project_data_in)
    except Exception:
        raise HTTPException(
            status_code=400, detail="ProjectData with this ID already exists"
        )

    return {"success": True, "data": project_data}


@router.get("/{id}", response_model=schemas.ProjectDataResponse)
async def get_project_data(
    id: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """Get project_data by ID."""
    r = crud.project_data.get(db, id)
    if not r:
        raise HTTPException(status_code=404, detail="ProjectData not found")

    return {"success": True, "data": r}


@router.put("/{id}", response_model=schemas.ProjectDataResponse)
async def update_project_data(
    id: uuid.UUID,
    project_data_in: schemas.ProjectDataUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update a project_data.
    """
    project_data = crud.project_data.get(db=db, id=id)
    if not project_data:
        raise HTTPException(status_code=404, detail="ProjectData not found")

    project_data = crud.project_data.update(
        db=db, db_obj=project_data, obj_in=project_data_in
    )

    return {"success": True, "data": project_data}


@router.delete("/{id}", response_model=schemas.ProjectDataResponse)
async def delete_project_data(
    id: uuid.UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete a project_data.
    """
    project_data = crud.project_data.get(db=db, id=id)
    if not project_data:
        raise HTTPException(status_code=404, detail="ProjectData not found")

    project_data = crud.project_data.remove(db=db, id=id)

    return {"success": True, "data": project_data}


@router.get("/", response_model=schemas.ProjectDataListResponse)
async def list_project_datas(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve project_datas.
    """
    rows = crud.project_data.get_multi(db, limit=1000)

    return {"success": True, "data": rows}
