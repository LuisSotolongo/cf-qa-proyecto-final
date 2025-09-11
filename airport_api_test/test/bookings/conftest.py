# import os
# import random
# import string
# import requests, pytest
# from faker import Faker
# from dotenv import load_dotenv
# from ...utils.api_helpers import api_request
# from ...utils.settings import USERS, AUTH_LOGIN, AIRPORTS
# from datetime import datetime, timedelta
#
# fake = Faker()
# load_dotenv()
# BASE_URL = os.getenv("BASE_URL")
#
# @pytest.fixture
# def flight_id(auth_headers):
#     now = datetime.utcnow()
#     flight_data = {
#         "origin": "AAA",
#         "destination": "BBB",
#         "departure_time": (now + timedelta(days=1)).isoformat() + "Z",
#         "arrival_time": (now + timedelta(days=1, hours=2)).isoformat() + "Z",
#         "base_price": 100,
#         "aircraft_id": "AC123"
#     }
#     response = api_request("post", URL + FLIGHTS, json=flight_data, headers=auth_headers)
#     return response.json()["id"]
#
# @pytest.fixture
# def booking_data(flight_id):
#     row = random.randint(1, 50)
#     seat_letter = random.choice("ABCDEF")
#     return {
#         "flight_id": flight_id,
#         "passengers": [
#             {
#                 "full_name": fake.name(),
#                 "passport": fake.bothify(text="??######"),
#                 "seat": f"{row}{seat_letter}"
#             }
#         ]
#     }