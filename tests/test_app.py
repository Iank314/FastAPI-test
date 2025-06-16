# tests/test_app.py
import os
# Set environment variables for BaseSettings
os.environ['DATABASE_URL'] = "sqlite:///./test.db"
os.environ['SECRET_KEY'] = "testsecret"
os.environ['ACCESS_TOKEN_EXPIRE_MINUTES'] = "60"
os.environ['ALGORITHM'] = "HS256"

import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_register_login_and_project_flow():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Register a new user
        resp = await ac.post(
            "/auth/register",
            json={"email": "test@example.com", "password": "password"}
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["email"] == "test@example.com"

        # Login
        resp = await ac.post(
            "/auth/login",
            json={"email": "test@example.com", "password": "password"}
        )
        assert resp.status_code == 200
        token = resp.json()["access_token"]
        assert token

        headers = {"Authorization": f"Bearer {token}"}

        # Create a project
        project_payload = {"name": "Proj", "description": "Desc"}
        resp = await ac.post("/projects", headers=headers, json=project_payload)
        assert resp.status_code == 200
        proj = resp.json()
        assert proj["name"] == project_payload["name"]

        # List projects
        resp = await ac.get("/projects", headers=headers)
        assert resp.status_code == 200
        projs = resp.json()
        assert isinstance(projs, list)
        assert any(p["id"] == proj["id"] for p in projs)
