from uuid import UUID, uuid4
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List

class Comment(SQLModel, table=True):
    __tablename__ = "comments"

    id: UUID           = Field(default_factory=uuid4, primary_key=True, index=True)
    task_id: UUID      = Field(foreign_key="tasks.id", nullable=False, index=True)
    author_id: UUID    = Field(foreign_key="users.id", nullable=False, index=True)
    body: str          = Field(...)

    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    task: "Task" = Relationship(back_populates="comments")
    author: "User" = Relationship(back_populates="comments")
