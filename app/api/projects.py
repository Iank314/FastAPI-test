from __future__ import annotations

from uuid import UUID
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate
from app.crud.project    import (
    create_project, get_project, get_projects_by_owner,
    update_project, delete_project,
)
from app.api.deps        import get_db, get_current_user

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("", response_model=ProjectRead)
def create_new_project(
    proj_in: ProjectCreate,
    current = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return create_project(db, current.id, proj_in)


@router.get("", response_model=List[ProjectRead])
def read_projects(
    current = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_projects_by_owner(db, current.id)


@router.get("/{project_id}", response_model=ProjectRead)
def read_project(
    project_id: UUID,
    current = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    proj = get_project(db, project_id)
    if not proj or proj.owner_id != current.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return proj


@router.patch("/{project_id}", response_model=ProjectRead)
def edit_project(
    project_id: UUID,
    proj_in:   ProjectUpdate,
    current = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    proj = get_project(db, project_id)
    if not proj or proj.owner_id != current.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return update_project(db, proj, proj_in)


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_project(
    project_id: UUID,
    current = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    proj = get_project(db, project_id)
    if not proj or proj.owner_id != current.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    delete_project(db, proj)
