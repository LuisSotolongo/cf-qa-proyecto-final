import os
import random
import string
import requests, pytest
from faker import Faker
from dotenv import load_dotenv
from ...utils.api_helpers import api_request
from ...utils.settings import USERS, AUTH_LOGIN, AIRPORTS


fake = Faker()
load_dotenv()
BASE_URL = os.getenv("BASE_URL")

@pytest.fixture
def airport_data():
    return {
        "iata_code": "".join(random.choices(string.ascii_uppercase, k=3)),
        "city": "Las Palmas",
        "country": fake.country_code(),
    }

@pytest.fixture
def airport(auth_headers, airport_data):
        response = api_request("post", BASE_URL + AIRPORTS, json=airport_data, headers=auth_headers)
        response.raise_for_status()
        airport_response = response.json()
        yield airport_response
        delete_response = api_request("delete", BASE_URL + f'/airports/{airport_response["iata_code"]}', headers=auth_headers)
        delete_response.raise_for_status()



def test_airport(airport):
    print(airport)
