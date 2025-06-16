from __future__ import annotations

from uuid import UUID
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate, TaskRead, TaskUpdate
from app.crud.task    import (
    create_task, get_task, get_tasks,
    update_task, delete_task,
)
from app.api.deps     import get_db, get_current_user

router = APIRouter(tags=["tasks"])


@router.post("/projects/{project_id}/tasks", response_model=TaskRead)
def add_task(
    project_id: UUID,
    task_in:    TaskCreate,
    current = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return create_task(db, project_id, task_in)


@router.get("/projects/{project_id}/tasks", response_model=List[TaskRead])
def list_tasks(
    project_id: UUID,
    status: Optional[str] = None,
    current = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_tasks(db, project_id, status)


@router.get("/tasks/{task_id}", response_model=TaskRead)
def get_single_task(
    task_id: UUID,
    current = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return task


@router.patch("/tasks/{task_id}", response_model=TaskRead)
def modify_task(
    task_id: UUID,
    task_in: TaskUpdate,
    current = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return update_task(db, task, task_in)


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_task(
    task_id: UUID,
    current = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    delete_task(db, task)
