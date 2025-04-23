from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from ..database import Base

class AssetSharing(Base):
    __tablename__ = "asset_sharing"

    id = Column(Integer, primary_key=True, index=True)
    asset_id = Column(Integer, ForeignKey("assets.id"), nullable=False)
    shared_with = Column(String, nullable=False)
    access_level = Column(String, nullable=True)
    shared_on = Column(DateTime(timezone=True), server_default=func.now())
    shared_by = Column(String, nullable=True)
    updated_on = Column(DateTime(timezone=True), onupdate=func.now())
    updated_by = Column(String, nullable=True)