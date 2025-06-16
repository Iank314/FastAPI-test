from sqlalchemy.orm import Session
from typing import List
from app.schemas.comment import CommentCreate
from app.models.comment import Comment

def create_comment(db: Session, task_id: str, author_id: str, com_in: CommentCreate) -> Comment:
    com = Comment(task_id=task_id, author_id=author_id, **com_in.dict())
    db.add(com)
    db.commit()
    db.refresh(com)
    return com


def get_comments(db: Session, task_id: str) -> List[Comment]:
    return db.query(Comment).filter(Comment.task_id == task_id).all()