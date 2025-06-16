from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from uuid import UUID
from app.models.task import TaskStatus

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to: Optional[UUID] = None
    due_date: Optional[date] = None

class TaskRead(BaseModel):
    id: UUID
    project_id: UUID
    title: str
    description: Optional[str]
    assigned_to: Optional[UUID]
    due_date: Optional[date]
    status: TaskStatus
    created_at: datetime

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    assigned_to: Optional[UUID] = None
    due_date: Optional[date] = None
    status: Optional[TaskStatus] = None

