import pytest
import requests
import os
import random
from dotenv import load_dotenv
from datetime import datetime, timedelta
from faker import Faker
from ..utils.settings import  AUTH_LOGIN, FLIGHTS, BOOKINGS
from ..utils.api_helpers import api_request

load_dotenv()
fake = Faker()
BASE_URL = os.getenv("BASE_URL")

@pytest.fixture(scope="session", autouse=True)
def admin_token() -> str:
    user = os.getenv("ADMIN_USER")
    password = os.getenv("ADMIN_PASSWORD")
    response = requests.post(
        BASE_URL + AUTH_LOGIN, data ={"username": user, "password": password}, timeout=5)
    response.raise_for_status()
    return response.json()["access_token"]


@pytest.fixture
def auth_headers(admin_token):
    return {
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def flight_data():
    now = datetime.utcnow()
    return {
        "origin": "AAA",
        "destination": "BBB",
        "departure_time": (now + timedelta(days=1)).isoformat() + "Z",
        "arrival_time": (now + timedelta(days=1, hours=2)).isoformat() + "Z",
        "base_price": 100,
        "aircraft_id": "AC123"
    }

@pytest.fixture
def flight_id(auth_headers, flight_data):
    response = api_request("post", BASE_URL + FLIGHTS, json=flight_data, headers=auth_headers)
    return response.json()["id"]


@pytest.fixture
def booking_data(flight_id):
    row = random.randint(1, 50)
    seat_letter = random.choice("ABCDEF")
    return {
        "flight_id": flight_id,
        "passengers": [
            {
                "full_name": fake.name(),
                "passport": fake.bothify(text="??######"),
                "seat": f"{row}{seat_letter}"
            }
        ]
    }