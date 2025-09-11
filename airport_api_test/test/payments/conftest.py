import pytest
import os
import requests
from jsonschema import validate
from dotenv import load_dotenv
from ...utils.api_helpers import api_request
from ...utils.settings import USERS, AUTH_LOGIN, AIRPORTS
from datetime import datetime, timedelta

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
FLIGHTS = "/flights"
BOOKINGS = "/bookings"


# @pytest.fixture
# def booking_id(auth_headers):
#     now = datetime.utcnow()
#     flight_data = {
#         "origin": "AAA",
#         "destination": "BBB",
#         "departure_time": (now + timedelta(days=1)).isoformat() + "Z",
#         "arrival_time": (now + timedelta(days=1, hours=2)).isoformat() + "Z",
#         "base_price": 100,
#         "aircraft_id": "AC123"
#     }
#     flight_resp = api_request("post", URL + FLIGHTS, json=flight_data, headers=auth_headers)
#     flight_id = flight_resp.json()["id"]
#     booking_data = {
#         "flight_id": flight_id,
#         "passengers": [
#             {"full_name": "Juan Perez", "passport": "A1234567", "seat": "12A"}
#         ]
#     }
#     booking_resp = api_request("post", URL + BOOKINGS, json=booking_data, headers=auth_headers)
#     return booking_resp.json()["id"]


@pytest.fixture
def payment_data(booking_id):
    return {
        "booking_id": booking_id,
        "amount": 100,
        "payment_method": "credit_card"
    }
