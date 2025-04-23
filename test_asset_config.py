import pytest
from fastapi.testclient import TestClient
from asset_api.main import app
from asset_api.database import get_db
from asset_api.models.asset_config import AssetConfig
from asset_api.schemas.asset_config import AssetConfigCreate
from sqlalchemy.orm import Session

client = TestClient(app)

def override_get_db():
    from asset_api.database import SessionLocal
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function")
def db_session():
    from asset_api.database import SessionLocal
    db = SessionLocal()
    yield db
    db.query(AssetConfig).delete()
    db.commit()
    db.close()

def test_create_asset_config(db_session):
    data = {"name": "Test Config", "value": "123"}
    response = client.post("/asset_config/", json=data)
    assert response.status_code == 201 or response.status_code == 200
    resp_json = response.json()
    assert resp_json["name"] == data["name"]
    assert resp_json["value"] == data["value"]
    db_obj = db_session.query(AssetConfig).filter_by(id=resp_json["id"]).first()
    assert db_obj is not None
    assert db_obj.name == data["name"]
    assert db_obj.value == data["value"]

def test_get_asset_config(db_session):
    asset_config = AssetConfig(name="GetTest", value="abc")
    db_session.add(asset_config)
    db_session.commit()
    db_session.refresh(asset_config)
    response = client.get(f"/asset_config/{asset_config.id}")
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["id"] == asset_config.id
    assert resp_json["name"] == asset_config.name
    assert resp_json["value"] == asset_config.value

def test_update_asset_config(db_session):
    asset_config = AssetConfig(name="UpdateTest", value="old")
    db_session.add(asset_config)
    db_session.commit()
    db_session.refresh(asset_config)
    update_data = {"name": "Updated", "value": "new"}
    response = client.put(f"/asset_config/{asset_config.id}", json=update_data)
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json["name"] == update_data["name"]
    assert resp_json["value"] == update_data["value"]
    db_obj = db_session.query(AssetConfig).filter_by(id=asset_config.id).first()
    assert db_obj.name == update_data["name"]
    assert db_obj.value == update_data["value"]

def test_delete_asset_config(db_session):
    asset_config = AssetConfig(name="DeleteTest", value="del")
    db_session.add(asset_config)
    db_session.commit()
    db_session.refresh(asset_config)
    response = client.delete(f"/asset_config/{asset_config.id}")
    assert response.status_code == 200 or response.status_code == 204
    db_obj = db_session.query(AssetConfig).filter_by(id=asset_config.id).first()
    assert db_obj is None

def test_list_asset_configs(db_session):
    db_session.add_all([
        AssetConfig(name="List1", value="v1"),
        AssetConfig(name="List2", value="v2")
    ])
    db_session.commit()
    response = client.get("/asset_config/")
    assert response.status_code == 200
    resp_json = response.json()
    assert isinstance(resp_json, list)
    assert len(resp_json) >= 2
    names = [item["name"] for item in resp_json]
    assert "List1" in names and "List2" in names