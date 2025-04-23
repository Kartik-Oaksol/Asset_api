from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AssetConfigCreate(BaseModel):
    config_name: str
    config_value: Optional[dict] = None

class AssetConfigUpdate(BaseModel):
    config_name: Optional[str] = None
    config_value: Optional[dict] = None

class AssetConfigResponse(BaseModel):
    id: int
    config_name: str
    config_value: Optional[dict] = None
    created_on: datetime
    created_by: Optional[str] = None
    updated_on: Optional[datetime] = None
    updated_by: Optional[str] = None

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class AssetConfigOut(BaseModel):
    id: int
    config_name: str
    config_value: Optional[dict] = None
    created_on: datetime
    created_by: Optional[str] = None
    updated_on: Optional[datetime] = None
    updated_by: Optional[str] = None

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }