# # airport_api_test/test/flights/conftest.py
#
# import pytest
# from ...utils.api_helpers import api_request
# from datetime import datetime, timedelta
#
# URL = "http://localhost:8000"
# FLIGHTS = "/flights"
#
#
# @pytest.fixture
# def flight_data():
#     now = datetime.utcnow()
#     return {
#         "origin": "AAA",
#         "destination": "BBB",
#         "departure_time": (now + timedelta(days=1)).isoformat() + "Z",
#         "arrival_time": (now + timedelta(days=1, hours=2)).isoformat() + "Z",
#         "base_price": 100,
#         "aircraft_id": "AC123"
#     }
#
# @pytest.fixture
# def flight_id(auth_headers, flight_data):
#     response = api_request("post", URL + FLIGHTS, json=flight_data, headers=auth_headers)
#     return response.json()["id"]
