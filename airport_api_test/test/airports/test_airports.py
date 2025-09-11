import pytest
import os
import requests
from jsonschema import validate
from dotenv import load_dotenv
from ...utils.api_helpers import api_request
from ...utils.settings import USERS, AUTH_LOGIN, AIRPORTS

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

airport_shema = {
    "type": "object",
    "required": ["iata_code", "city","country"],
    "properties": {
         "iata_code": {"type": "string", "minLength": 3, "maxLength": 3},
            "city": {"type": "string"},
            "country": {"type": "string"},
    },
    "additionalProperties": False
}


def test_create_json_schema(airport):
    validate(instance=airport, schema=airport_shema)

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_get_all_airports(airport, auth_headers, skip=0, limit=10):
    url = f"{BASE_URL}{AIRPORTS}?skip={skip}&limit={limit}"
    response = api_request("get", url, headers=auth_headers)
    lista = response.text
    assert response.status_code == 200
    assert response.json() != []
    assert lista

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_create_airport_success(auth_headers, airport_data):
    iata_code = airport_data["iata_code"]
    response = api_request("post", BASE_URL + AIRPORTS, json=airport_data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["iata_code"] == iata_code

# Falta iata_code y country
def test_create_airport_invalid(auth_headers):
    data = {"city": "Las Palmas"}
    response = api_request("post", BASE_URL + AIRPORTS, json=data, headers=auth_headers)
    assert response.status_code == 422

def test_get_airports_success(auth_headers):
    response = api_request("get", BASE_URL + AIRPORTS, headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_airport_not_found(auth_headers):
    response = api_request("get", BASE_URL + AIRPORTS + "/LOST", headers=auth_headers)
    assert response.status_code in [404, 422]

def test_update_airport_success(auth_headers):
    data = {"iata_code": "LPA", "city": "Madrid", "country": "ES"}
    response = api_request("put", BASE_URL + AIRPORTS + "/LPA", json=data, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["city"] == "Madrid"

# Falta iata_code y country
def test_update_airport_invalid(auth_headers):
    data = {"city": "Barcelona"}
    response = api_request("put", BASE_URL + AIRPORTS + "/ABC", json=data, headers=auth_headers)
    assert response.status_code == 422

def test_delete_airport_success(auth_headers):
    response = api_request("delete", BASE_URL + AIRPORTS + "/ABC", headers=auth_headers)
    assert response.status_code == 204

def test_delete_airport_invalid(auth_headers):
    response = api_request("delete", BASE_URL + AIRPORTS + "/ZZZ", headers=auth_headers)
    assert response.status_code == 204


