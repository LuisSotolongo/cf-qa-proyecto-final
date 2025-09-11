import pytest
import os
import requests
from jsonschema import validate
from dotenv import load_dotenv
from ...utils.api_helpers import api_request
from ...utils.settings import USERS, AUTH_LOGIN, AIRPORTS

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
BOOKINGS = "/bookings"



def test_create_booking_success(auth_headers, booking_data):
    response = api_request("post", BASE_URL + BOOKINGS, json=booking_data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["flight_id"] == booking_data["flight_id"]

def test_create_booking_invalid(auth_headers):
    data = {"passengers": []}  # Falta flight_id y pasajeros vacíos
    response = api_request("post", BASE_URL + BOOKINGS, json=data, headers=auth_headers)
    assert response.status_code == 422

def test_get_bookings_success(auth_headers):
    response = api_request("get", BASE_URL + BOOKINGS, headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Primero crea la reserva
def test_get_booking_success(auth_headers, booking_data):
    create_resp = api_request("post", BASE_URL + BOOKINGS, json=booking_data, headers=auth_headers)
    booking_id = create_resp.json()["id"]
    response = api_request("get", BASE_URL + BOOKINGS + f"/{booking_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == booking_id

def test_get_booking_not_found(auth_headers):
    response = api_request("get", BASE_URL + BOOKINGS + "/noexiste", headers=auth_headers)
    assert response.status_code == 422

def test_update_booking_success(auth_headers, booking_data):
    create_resp = api_request("post", BASE_URL + BOOKINGS, json=booking_data, headers=auth_headers)
    booking_id = create_resp.json()["id"]
    update_data = {"status": "confirmed"}
    response = api_request("patch", BASE_URL + BOOKINGS + f"/{booking_id}", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["status"] == "confirmed"

def test_update_booking_invalid(auth_headers):
    response = api_request("patch", BASE_URL + BOOKINGS + "/noexiste", json={"status": "confirmed"}, headers=auth_headers)
    assert response.status_code == 422

def test_delete_booking_success(auth_headers, booking_data):
    create_resp = api_request("post", BASE_URL + BOOKINGS, json=booking_data, headers=auth_headers)
    booking_id = create_resp.json()["id"]
    response = api_request("delete", BASE_URL + BOOKINGS + f"/{booking_id}", headers=auth_headers)
    assert response.status_code == 204

def test_delete_booking_invalid(auth_headers):
    response = api_request("delete", BASE_URL + BOOKINGS + "/noexiste", headers=auth_headers)
    assert response.status_code == 422
