from fastapi import FastAPI
from asset_api.routes import asset, folder, asset_sharing, asset_config
from asset_api.database import engine
from asset_api.models import asset as asset_model

app = FastAPI(title="Asset API", description="CRUD API for Asset management", version="1.0.0")

# Auto-create tables
asset_model.Base.metadata.create_all(bind=engine)

# Include asset routes
app.include_router(asset.router)
app.include_router(folder.router)
app.include_router(asset_sharing.router)
app.include_router(asset_config.router)