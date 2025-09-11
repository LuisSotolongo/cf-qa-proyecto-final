import os
import requests
import pytest
from jsonschema import validate
from dotenv import load_dotenv
from ...utils.api_helpers import api_request
from ...utils.settings import AIRCRAFTS
from ...utils.api_helpers import api_request

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

def test_create_aircraft_success(auth_headers, aircraft_data):
    resp = api_request("post", BASE_URL + AIRCRAFTS, json=aircraft_data, headers=auth_headers)
    assert resp.status_code == 201
    assert resp.json()["tail_number"] == aircraft_data["tail_number"]
 # Falta tail_number y capacity
def test_create_aircraft_invalid(auth_headers):
    data = {"model": "Boeing 737"}
    resp = api_request("post", BASE_URL + AIRCRAFTS, json=data, headers=auth_headers)
    assert resp.status_code == 422


def test_get_aircraft_success(auth_headers, aircraft_id):
    resp = api_request("get", BASE_URL + AIRCRAFTS + f"/{aircraft_id}", headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["id"] == aircraft_id

def test_get_aircraft_invalid(auth_headers):
    resp = api_request("get", BASE_URL + AIRCRAFTS + "/noexiste", headers=auth_headers)
    assert resp.status_code == 404

def test_update_aircraft_success(auth_headers, aircraft_id):
    update_data = {"tail_number": "N54321", "model": "Airbus A320", "capacity": 150}
    resp = api_request("put", BASE_URL + AIRCRAFTS + f"/{aircraft_id}", json=update_data, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["tail_number"] == "N54321"
 # Falta tail_number y capacity
def test_update_aircraft_invalid(auth_headers, aircraft_id):
    data = {"model": "Airbus A320"}
    resp = api_request("put", BASE_URL + AIRCRAFTS + f"/{aircraft_id}", json=data, headers=auth_headers)
    assert resp.status_code == 422

def test_delete_aircraft_success(auth_headers, aircraft_id):
    resp = api_request("delete", BASE_URL + AIRCRAFTS + f"/{aircraft_id}", headers=auth_headers)
    assert resp.status_code == 204

def test_delete_aircraft_invalid(auth_headers):
    resp = api_request("delete", BASE_URL + AIRCRAFTS + "/errornoexiste", headers=auth_headers)
    if resp.status_code == 204:
        pytest.fail("Aunque el aircraft_id no existe la respuesta es 204")
    assert resp.status_code == 422
