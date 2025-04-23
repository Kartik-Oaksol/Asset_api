Asset Management Backend System

A backend system for asset management built using FastAPI and PostgreSQL, supporting full CRUD operations for:

- Folders
- Asset Sharing
- Asset Config

 Features

- Modular FastAPI structure
- PostgreSQL DB integration via SQLAlchemy
- Pydantic schema validation
- Swagger UI for easy testing at `/docs`
- Easily extensible and production-ready

 Folder Structure

asset_api/
├── main.py
├── models/
│   ├── folder.py
│   ├── asset_sharing.py
│   └── asset_config.py
├── routes/
│   ├── folder.py
│   ├── asset_sharing.py
│   └── asset_config.py
├── schemas/
│   ├── folder.py
│   ├── asset_sharing.py
│   └── asset_config.py


 Setup Instructions

1. Clone the repo**
   bash
   git clone https://github.com/Kartik-Oaksol/Asset_api.git
   cd Asset_api
   

2. Install dependencies**
   bash
   pip install -r requirements.txt
   

3. Set your PostgreSQL URL**
   
   Update your `DATABASE_URL` inside your environment or config:
   
   
   postgresql://<user>:<password>@localhost:5432/<database_name>
   

4. Run the API**
   bash
   uvicorn asset_api.main:app --reload
   

API Documentation

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore:

 Folders
- `GET /folders/` — List all folders
- `POST /folders/` — Create folder
- `GET /folders/{folder_id}` — Get folder by ID
- `PUT /folders/{folder_id}` — Update folder
- `DELETE /folders/{folder_id}` — Delete folder

 Asset Sharing
- `POST /asset_sharing/`
- `GET /asset_sharing/{asset_sharing_id}`
- `PUT /asset_sharing/{asset_sharing_id}`
- `DELETE /asset_sharing/{asset_sharing_id}`

 Asset Config
- `POST /asset_config/`
- `GET /asset_config/{asset_config_id}`
- `PUT /asset_config/{asset_config_id}`
- `DELETE /asset_config/{asset_config_id}`