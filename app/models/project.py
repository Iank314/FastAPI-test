from uuid import UUID, uuid4
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List

class Project(SQLModel, table=True):
    __tablename__ = "projects"

    id: UUID           = Field(default_factory=uuid4, primary_key=True, index=True)
    owner_id: UUID     = Field(foreign_key="users.id", nullable=False, index=True)
    name: str          = Field(..., max_length=100)
    description: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    owner: "User" = Relationship(back_populates="projects")
    tasks: List["Task"] = Relationship(back_populates="project")
