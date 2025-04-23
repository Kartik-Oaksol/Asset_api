from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.folder import Folder
from ..schemas.folder import FolderCreate, FolderUpdate, FolderResponse

router = APIRouter(prefix="/folders", tags=["Folders"])

@router.post("/", response_model=FolderResponse)
def create_folder(folder: FolderCreate, db: Session = Depends(get_db)):
    db_folder = Folder(**folder.dict())
    db.add(db_folder)
    db.commit()
    db.refresh(db_folder)
    return db_folder

@router.get("/", response_model=list[FolderResponse])
def list_folders(db: Session = Depends(get_db)):
    folders = db.query(Folder).all()
    return folders

@router.get("/{folder_id}", response_model=FolderResponse)
def get_folder(folder_id: int, db: Session = Depends(get_db)):
    folder = db.query(Folder).filter(Folder.id == folder_id).first()
    if not folder:
        raise HTTPException(status_code=404, detail="Folder not found")
    return folder

@router.put("/{folder_id}", response_model=FolderResponse)
def update_folder(folder_id: int, folder: FolderUpdate, db: Session = Depends(get_db)):
    db_folder = db.query(Folder).filter(Folder.id == folder_id).first()
    if not db_folder:
        raise HTTPException(status_code=404, detail="Folder not found")
    for key, value in folder.dict(exclude_unset=True).items():
        setattr(db_folder, key, value)
    db.commit()
    db.refresh(db_folder)
    return db_folder

@router.delete("/{folder_id}", response_model=FolderResponse)
def delete_folder(folder_id: int, db: Session = Depends(get_db)):
    folder = db.query(Folder).filter(Folder.id == folder_id).first()
    if not folder:
        raise HTTPException(status_code=404, detail="Folder not found")
    db.delete(folder)
    db.commit()
    return folder