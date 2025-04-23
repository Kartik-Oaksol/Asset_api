from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.asset_sharing import AssetSharing
from ..schemas.asset_sharing import AssetSharingCreate, AssetSharingUpdate, AssetSharingResponse

router = APIRouter(prefix="/asset_sharing", tags=["Asset Sharing"])

@router.post("/", response_model=AssetSharingResponse)
def create_asset_sharing(asset_sharing: AssetSharingCreate, db: Session = Depends(get_db)):
    # Validate asset_id exists before proceeding
    asset = db.query(AssetSharing.__table__.metadata.tables['assets']).filter_by(id=asset_sharing.asset_id).first()
    if not asset:
        raise HTTPException(status_code=400, detail=f"Asset with id {asset_sharing.asset_id} does not exist.")
    try:
        db_asset_sharing = AssetSharing(**asset_sharing.dict())
        db.add(db_asset_sharing)
        db.commit()
        db.refresh(db_asset_sharing)
        return db_asset_sharing
    except Exception as e:
        db.rollback()
        from sqlalchemy.exc import IntegrityError
        if isinstance(e, IntegrityError):
            raise HTTPException(status_code=400, detail="Invalid asset_id or integrity error: " + str(e.orig))
        raise HTTPException(status_code=500, detail="Internal Server Error: " + str(e))

@router.get("/", response_model=list[AssetSharingResponse])
def list_asset_sharing(db: Session = Depends(get_db)):
    asset_sharing_records = db.query(AssetSharing).all()
    return asset_sharing_records

@router.get("/{asset_sharing_id}", response_model=AssetSharingResponse)
def get_asset_sharing(asset_sharing_id: int, db: Session = Depends(get_db)):
    asset_sharing = db.query(AssetSharing).filter(AssetSharing.id == asset_sharing_id).first()
    if not asset_sharing:
        raise HTTPException(status_code=404, detail="Asset Sharing not found")
    return asset_sharing

@router.put("/{asset_sharing_id}", response_model=AssetSharingResponse)
def update_asset_sharing(asset_sharing_id: int, asset_sharing: AssetSharingUpdate, db: Session = Depends(get_db)):
    db_asset_sharing = db.query(AssetSharing).filter(AssetSharing.id == asset_sharing_id).first()
    if not db_asset_sharing:
        raise HTTPException(status_code=404, detail="Asset Sharing not found")
    for key, value in asset_sharing.dict(exclude_unset=True).items():
        setattr(db_asset_sharing, key, value)
    db.commit()
    db.refresh(db_asset_sharing)
    return db_asset_sharing

@router.delete("/{asset_sharing_id}", response_model=AssetSharingResponse)
def delete_asset_sharing(asset_sharing_id: int, db: Session = Depends(get_db)):
    asset_sharing = db.query(AssetSharing).filter(AssetSharing.id == asset_sharing_id).first()
    if not asset_sharing:
        raise HTTPException(status_code=404, detail="Asset Sharing not found")
    db.delete(asset_sharing)
    db.commit()
    return asset_sharing