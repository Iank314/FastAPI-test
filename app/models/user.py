from uuid import UUID, uuid4
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    email: str = Field(..., unique=True, index=True)
    hashed_password: str = Field(..., nullable=False)
    joined_at: datetime  = Field(default_factory=datetime.utcnow, nullable=False)

    projects: List["Project"] = Relationship(back_populates="owner")
    comments: List["Comment"] = Relationship(back_populates="author")