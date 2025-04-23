from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.asset_config import AssetConfig
from ..schemas.asset_config import AssetConfigCreate, AssetConfigUpdate, AssetConfigResponse
from ..schemas.asset_config import AssetConfigOut

router = APIRouter(prefix="/asset_config", tags=["Asset Config"])

@router.post("/", response_model=AssetConfigResponse)
def create_asset_config(asset_config: AssetConfigCreate, db: Session = Depends(get_db)):
    db_asset_config = AssetConfig(**asset_config.dict())
    db.add(db_asset_config)
    db.commit()
    db.refresh(db_asset_config)
    return db_asset_config

@router.get("/", response_model=list[AssetConfigOut])
def list_asset_configs(db: Session = Depends(get_db)):
    asset_configs = db.query(AssetConfig).all()
    return asset_configs

@router.get("/{asset_config_id}", response_model=AssetConfigResponse)
def get_asset_config(asset_config_id: int, db: Session = Depends(get_db)):
    asset_config = db.query(AssetConfig).filter(AssetConfig.id == asset_config_id).first()
    if not asset_config:
        raise HTTPException(status_code=404, detail="Asset Config not found")
    return asset_config

@router.put("/{asset_config_id}", response_model=AssetConfigResponse)
def update_asset_config(asset_config_id: int, asset_config: AssetConfigUpdate, db: Session = Depends(get_db)):
    db_asset_config = db.query(AssetConfig).filter(AssetConfig.id == asset_config_id).first()
    if not db_asset_config:
        raise HTTPException(status_code=404, detail="Asset Config not found")
    for key, value in asset_config.dict(exclude_unset=True).items():
        setattr(db_asset_config, key, value)
    db.commit()
    db.refresh(db_asset_config)
    return db_asset_config

@router.delete("/{asset_config_id}", response_model=AssetConfigResponse)
def delete_asset_config(asset_config_id: int, db: Session = Depends(get_db)):
    asset_config = db.query(AssetConfig).filter(AssetConfig.id == asset_config_id).first()
    if not asset_config:
        raise HTTPException(status_code=404, detail="Asset Config not found")
    db.delete(asset_config)
    db.commit()
    return asset_config