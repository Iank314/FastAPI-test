from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.comment import CommentCreate, CommentRead
from app.crud.comment    import create_comment, get_comments
from app.api.deps        import get_db, get_current_user

router = APIRouter(prefix="/tasks", tags=["comments"])


@router.post("/{task_id}/comments", response_model=CommentRead)
def post_comment(
    task_id: UUID,
    com_in:  CommentCreate,
    current  = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return create_comment(db, task_id, current.id, com_in)


@router.get("/{task_id}/comments", response_model=List[CommentRead])
def read_comments(
    task_id: UUID,
    current  = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_comments(db, task_id)
