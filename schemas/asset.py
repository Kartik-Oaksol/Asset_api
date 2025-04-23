from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime

class AssetBase(BaseModel):
    name: str
    type: str
    asset_metadata: Optional[Any] = None
    security_level: Optional[str] = None
    access_level: Optional[str] = None
    is_leaf: Optional[bool] = False
    is_archived: Optional[bool] = False
    parent_id: Optional[int] = None
    child_id: Optional[int] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None

class AssetCreate(AssetBase):
    pass

class AssetUpdate(AssetBase):
    pass

class AssetOut(AssetBase):
    id: int
    created_on: Optional[datetime]
    updated_on: Optional[datetime]

    class Config:
        orm_mode = True