import os
import random
import string

import requests, pytest, faker
from dotenv import load_dotenv
from ...utils.settings import  USERS, AUTH_LOGIN

load_dotenv()
fake = faker.Faker()

@pytest.fixture
def user_data():
    return {
        "email": fake.unique.email(),
        "password": fake.password(),
        "full_name": fake.name(),
        "role": "admin"
    }

@pytest.fixture
def user(auth_headers, user_data):
    url = os.getenv("BASE_URL")
    response = requests.post(f"{url}{USERS}", json=user_data, headers=auth_headers, timeout=5)
    response.raise_for_status()
    user_created = response.json()
    yield user_created
    # Cleanup: delete the created user
    # delete_response = requests.delete(
    #     URL + f'/users/{user_created["user_id"]}', headers=auth_headers, timeout=5)
    # delete_response.raise_for_status()

