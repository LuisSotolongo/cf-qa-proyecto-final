import os
import requests
import pytest
from faker import Faker
from jsonschema import validate
from dotenv import load_dotenv
from ...utils.api_helpers import api_request
from ...utils.settings import AIRCRAFTS
from ...utils.api_helpers import api_request

load_dotenv()
fake = Faker()
BASE_URL = os.getenv("BASE_URL")


@pytest.fixture
def aircraft_data():
        return {
        "tail_number": fake.bothify(text="N#####"),
        "model": fake.random_element(elements=["Boeing 737", "Airbus A320", "Embraer 190"]),
        "capacity": fake.random_int(min=100, max=300)
    }

@pytest.fixture
def aircraft_id(auth_headers, aircraft_data):
    resp = api_request("post", BASE_URL + AIRCRAFTS, json=aircraft_data, headers=auth_headers)
    return resp.json()["id"]
