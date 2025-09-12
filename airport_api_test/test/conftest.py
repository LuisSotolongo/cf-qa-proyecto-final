import pytest
import requests
import os
import random
import string
from dotenv import load_dotenv
from datetime import datetime, timedelta
from faker import Faker
from ..utils.settings import  AUTH_LOGIN, USERS, AIRCRAFTS, FLIGHTS, BOOKINGS, PAYMENTS, AIRPORTS
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


@pytest.fixture(scope="function")
def flight_data(create_aircraft):
    now = datetime.utcnow()
    return {
        "origin": "AAA",
        "destination": "BBB",
        "departure_time": (now + timedelta(days=1)).isoformat() + "Z",
        "arrival_time": (now + timedelta(days=1, hours=2)).isoformat() + "Z",
        "base_price": 100,
        "aircraft_id": create_aircraft
    }

@pytest.fixture(scope="function")
def airport_create_data():
    return {
        "iata_code": fake.unique.lexify(text="???", letters=string.ascii_uppercase),
        "city": fake.city(),
        "country": fake.country_code(representation="alpha-2")
    }


@pytest.fixture(scope="function")
def create_user(auth_headers):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    unique_email = f"test_{timestamp}_{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}@example.com"
    user_data = {
        "email": unique_email,
        "password": fake.password(),
        "full_name": fake.name(),
        "role": "passenger"
    }
    response = api_request("post", f"{BASE_URL}{USERS}", json=user_data, headers=auth_headers)
    response.raise_for_status()
    user_created = response.json()
    yield user_created
    # Borrado del usuario:
    api_request("delete", f"{BASE_URL}{USERS}/{user_created['id']}", headers=auth_headers)


@pytest.fixture(scope="session")
def login_request():
    def _login(username, password):
        return requests.post(os.getenv("BASE_URL") + AUTH_LOGIN, data={"username": username, "password": password}, timeout=5)
    return _login


@pytest.fixture(scope="function")
def create_aircraft(auth_headers):
    aircraft_data = {
        "tail_number": fake.bothify(text="N#####"),
        "model": fake.random_element(elements=["Boeing 737", "Airbus A320", "Embraer 190"]),
        "capacity": fake.random_int(min=100, max=300)
    }
    resp = api_request("post", BASE_URL + AIRCRAFTS, json=aircraft_data, headers=auth_headers)
    resp.raise_for_status()
    aircraft_id = resp.json()["id"]
    yield aircraft_id
    # Borrado de la avion:
    api_request("delete", f"{BASE_URL}{AIRCRAFTS}/{aircraft_id}", headers=auth_headers)


@pytest.fixture(scope="function")
def create_flight(auth_headers, flight_data):
    response = api_request("post", BASE_URL + FLIGHTS, json=flight_data, headers=auth_headers)
    response.raise_for_status()
    flight_id = response.json()["id"]
    yield flight_id
    # Borrado del vuelo:
    api_request("delete", f"{BASE_URL}{FLIGHTS}/{flight_id}", headers=auth_headers)




@pytest.fixture(scope="function")
def create_airport(auth_headers):
    airport_data = {
        "iata_code": fake.unique.lexify(text="???", letters=string.ascii_uppercase),
        "city": fake.city(),
        "country": fake.country_code(representation="alpha-2")
    }
    response = api_request("post", BASE_URL + AIRPORTS, json=airport_data, headers=auth_headers)
    response.raise_for_status()
    iata_code = response.json()["iata_code"]
    yield iata_code
    # Borrado del aeropuerto:
    api_request("delete", f"{BASE_URL}{AIRPORTS}/{iata_code}", headers=auth_headers)

@pytest.fixture(scope="session")
def airport_out_schema():
    return {
        "type": "object",
        "required": ["iata_code", "city", "country"],
        "properties": {
            "iata_code": {"type": "string", "minLength": 3, "maxLength": 3},
            "city": {"type": "string"},
            "country": {"type": "string"},
        },
        "additionalProperties": False
    }

@pytest.fixture(scope="function")
def airport_create_data():
    return {
        "iata_code": fake.unique.lexify(text="???", letters=string.ascii_uppercase),
        "city": fake.city(),
        "country": fake.country_code(representation="alpha-2")
    }

@pytest.fixture(scope="function")
def create_booking(auth_headers, create_flight, create_user):
    row = random.randint(1, 50)
    seat_letter = random.choice("ABCDEF")
    passenger_name = fake.name()
    passport = fake.bothify(text="??######")

    booking_data = {
        "flight_id": create_flight,
        "status": "draft",
        "passengers": [
            {
                "full_name": passenger_name,
                "passport": passport,
                "seat": f"{row}{seat_letter}"
            }
        ],
        "user_id": create_user["id"]
    }
    create_resp = api_request("post", BASE_URL + BOOKINGS, json=booking_data, headers=auth_headers)
    create_resp.raise_for_status()
    booking_id = create_resp.json()["id"]
    yield booking_id
    # Borrado del booking
    try:
        api_request("delete", f"{BASE_URL}{BOOKINGS}/{booking_id}", headers=auth_headers)
    except Exception as e:
        print(f"Error al eliminar booking {booking_id}: {e}")


@pytest.fixture(scope="function")
def create_payment(auth_headers, create_booking):
    payment_data = {
        "booking_id": create_booking,
        "amount": 100,
        "payment_method": "credit_card",
    }
    create_resp = api_request("post", BASE_URL + PAYMENTS, json=payment_data, headers=auth_headers)
    create_resp.raise_for_status()
    payment_id = create_resp.json()["id"]
    yield payment_id
    # Borrado del payment
    api_request("delete", f"{BASE_URL}{PAYMENTS}/{payment_id}", headers=auth_headers)
