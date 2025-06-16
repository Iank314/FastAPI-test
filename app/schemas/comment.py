from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional

class CommentCreate(BaseModel):
    body: str

class CommentRead(BaseModel):
    id: UUID
    task_id: UUID
    author_id: UUID
    body: str
    created_at: datetime

    class Config:
        orm_mode = True
