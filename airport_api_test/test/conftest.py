import pytest
import requests
import os
import random
import string
from dotenv import load_dotenv
from datetime import datetime, timedelta
from faker import Faker
from ..utils.settings import  AUTH_LOGIN, USERS, AIRCRAFTS, FLIGHTS, BOOKINGS
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


def random_email():
    return f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@example.com"

@pytest.fixture
def user_data():
    return {
        "email": random_email(),
        "password": fake.password(),
        "full_name": fake.name(),
        "role": "admin"
    }

@pytest.fixture
def user(auth_headers, user_data):
    url = os.getenv("BASE_URL")
    response = api_request("post", f"{BASE_URL}{USERS}", json=user_data, headers=auth_headers)
    response.raise_for_status()
    user_created = response.json()
    user_id_response = response.json()["id"]
    yield user_created
    # Cleanup: eliminar el usuario creado
    api_request("delete" ,f"{BASE_URL}{USERS}/{user_id_response}", headers=auth_headers)

@pytest.fixture
def user_id(user):
    return user["id"]


@pytest.fixture
def auth_headers(admin_token):
    return {
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }

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

@pytest.fixture
def flight_data(aircraft_id):
    now = datetime.utcnow()
    return {
        "origin": "AAA",
        "destination": "BBB",
        "departure_time": (now + timedelta(days=1)).isoformat() + "Z",
        "arrival_time": (now + timedelta(days=1, hours=2)).isoformat() + "Z",
        "base_price": 100,
        "aircraft_id": aircraft_id
    }

@pytest.fixture
def flight_id(auth_headers, flight_data):
    response = api_request("post", BASE_URL + FLIGHTS, json=flight_data, headers=auth_headers)
    return response.json()["id"]


@pytest.fixture
def booking_data(flight_id, user_id):
    row = random.randint(1, 50)
    seat_letter = random.choice("ABCDEF")
    return {
        "flight_id": flight_id,
        "user_id": user_id,
        "status": "draft",
        "passengers": [
            {
                "full_name": fake.name(),
                "passport": fake.bothify(text="??######"),
                "seat": f"{row}{seat_letter}"
            }
        ]
    }

@pytest.fixture
def booking_id(auth_headers, booking_data):
    create_resp = api_request("post", BASE_URL + BOOKINGS, json=booking_data, headers=auth_headers)
    return create_resp.json()["id"]


@pytest.fixture
def payment_data(booking_id):
    return {
        "booking_id": booking_id,
        "amount": 100,
        "payment_method": "credit_card",
        "status": "pending"
    }
