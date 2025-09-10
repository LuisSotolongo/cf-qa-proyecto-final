import os
import random
import string

import requests, pytest, faker
from dotenv import load_dotenv
from ...utils.settings import  USERS, AUTH_LOGIN

load_dotenv()
fake = faker.Faker()

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

@pytest.fixture
def user(auth_headers, role: str = "passenger"):
    url = os.getenv("BASE_URL")
    user_data = {
        "email": fake.email(),
        "full_name": fake.name(),
        "password": fake.password(),
        "role": role
    }
    response = requests.post(f"{url}{USERS}", json=user_data, headers=auth_headers, timeout=5)
    response.raise_for_status()
    user_created = response.json()
    yield user_created
    # Cleanup: delete the created user
    # delete_response = requests.delete(
    #     URL + f'/users/{user_created["user_id"]}', headers=auth_headers, timeout=5)
    # delete_response.raise_for_status()

def test_user(user):
    print(user)