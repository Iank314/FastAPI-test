from uuid import UUID
from datetime import datetime
from typing import Optional          
from pydantic import BaseModel, EmailStr   

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: UUID
    email: EmailStr                 
    joined_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: Optional[EmailStr] = None
