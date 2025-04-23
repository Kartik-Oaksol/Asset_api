from pydantic import BaseModel
from typing import Optional

class AssetSharingCreate(BaseModel):
    asset_id: int
    shared_with: str
    access_level: Optional[str] = None

class AssetSharingUpdate(BaseModel):
    shared_with: Optional[str] = None
    access_level: Optional[str] = None

class AssetSharingResponse(BaseModel):
    id: int
    asset_id: int
    shared_with: str
    access_level: Optional[str] = None
    shared_on: str
    shared_by: Optional[str] = None
    updated_on: Optional[str] = None
    updated_by: Optional[str] = None

    class Config:
        orm_mode = True