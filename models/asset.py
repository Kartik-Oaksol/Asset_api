from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from ..database import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    asset_metadata = Column(JSON, nullable=True)
    security_level = Column(String, nullable=True)
    access_level = Column(String, nullable=True)
    is_leaf = Column(Boolean, default=False)
    is_archived = Column(Boolean, default=False)
    parent_id = Column(Integer, ForeignKey("assets.id"), nullable=True)
    child_id = Column(Integer, ForeignKey("assets.id"), nullable=True)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(String, nullable=True)
    updated_on = Column(DateTime(timezone=True), onupdate=func.now())
    updated_by = Column(String, nullable=True)