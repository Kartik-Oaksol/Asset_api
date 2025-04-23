from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from ..database import Base

class AssetConfig(Base):
    __tablename__ = "asset_config"

    id = Column(Integer, primary_key=True, index=True)
    config_name = Column(String, nullable=False)
    config_value = Column(JSON, nullable=True)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(String, nullable=True)
    updated_on = Column(DateTime(timezone=True), onupdate=func.now())
    updated_by = Column(String, nullable=True)