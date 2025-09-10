import pytest
import requests
import os
from dotenv import load_dotenv
from ..utils.settings import  AUTH_LOGIN

load_dotenv()

@pytest.fixture(scope="session")
def admin_token() -> str:
    user = os.getenv("ADMIN_USER")
    password = os.getenv("ADMIN_PASSWORD")
    url = os.getenv("BASE_URL")
    response = requests.post(
        url + AUTH_LOGIN, data ={"username": user, "password": password}, timeout=5)
    response.raise_for_status()
    return response.json()["access_token"]



def test_admin_token(admin_token):
    return admin_token



@pytest.fixture
def auth_headers(admin_token):
    return {
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }