from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectRead(BaseModel):
    id: UUID
    owner_id: UUID
    name: str
    description: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
