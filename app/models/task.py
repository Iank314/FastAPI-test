from uuid import UUID, uuid4
from datetime import datetime, date
from enum import Enum
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from typing import List

class TaskStatus(str, Enum):
    todo        = "todo"
    in_progress = "in_progress"
    done        = "done"

class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    id: UUID             = Field(default_factory=uuid4, primary_key=True, index=True)
    project_id: UUID     = Field(foreign_key="projects.id", nullable=False, index=True)
    assigned_to: Optional[UUID] = Field(default=None, foreign_key="users.id", index=True)

    title: str          = Field(..., max_length=100)
    description: str | None = None
    status: TaskStatus  = Field(default=TaskStatus.todo, index=True)
    due_date: date | None   = None
    created_at: datetime    = Field(default_factory=datetime.utcnow, nullable=False)

    project: "Project" = Relationship(back_populates="tasks")
    comments: List["Comment"] = Relationship(back_populates="task")
