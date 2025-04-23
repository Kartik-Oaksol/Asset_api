from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FolderCreate(BaseModel):
    name: str
    description: Optional[str] = None

class FolderUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class FolderResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    created_on: datetime
    created_by: Optional[str] = None
    updated_on: Optional[datetime] = None
    updated_by: Optional[str] = None

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }