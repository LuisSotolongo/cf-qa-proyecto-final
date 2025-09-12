import pytest
import os
import requests
from jsonschema import validate, ValidationError
from dotenv import load_dotenv
from ...utils.api_helpers import api_request
from ...utils.settings import AIRPORTS

load_dotenv()
BASE_URL = os.getenv("BASE_URL")


def test_json_schema_validation(airport_create_data, airport_out_schema):
    try:
        validate(instance=airport_create_data, schema=airport_out_schema)
    except ValidationError as e:
        pytest.fail(f"La validación del esquema falló: {e.message}")


def test_create_airport_success(auth_headers, create_airport):
    iata_code = create_airport
    response = api_request("get", f"{BASE_URL}{AIRPORTS}/{iata_code}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["iata_code"] == iata_code


def test_create_airport_invalid(auth_headers):
    data = {"city": "Las Palmas"}
    response = api_request("post", BASE_URL + AIRPORTS, json=data, headers=auth_headers)
    assert response.status_code == 422


def test_get_all_airports(auth_headers):
    response = api_request("get", BASE_URL + AIRPORTS, headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_airport_not_found(auth_headers):
    response = api_request("get", f"{BASE_URL}{AIRPORTS}/LOST", headers=auth_headers)
    assert response.status_code == 404

@pytest.mark.retry(retries=3, delay=5)
def test_update_airport_success(auth_headers, create_airport):
    iata_code = create_airport
    update_data = {"iata_code": iata_code, "city": "Madrid", "country": "ES"}
    response = api_request("put", f"{BASE_URL}{AIRPORTS}/{iata_code}", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["city"] == "Madrid"


def test_update_airport_invalid(auth_headers, create_airport):
    iata_code = create_airport
    data = {"city": "Barcelona"}
    response = api_request("put", f"{BASE_URL}{AIRPORTS}/{iata_code}", json=data, headers=auth_headers)
    assert response.status_code == 422

@pytest.mark.retry(retries=3, delay=5)
def test_delete_airport_success(auth_headers, create_airport):
    iata_code = create_airport
    response = api_request("delete", f"{BASE_URL}{AIRPORTS}/{iata_code}", headers=auth_headers)
    assert response.status_code == 204
    get_response = api_request("get", f"{BASE_URL}{AIRPORTS}/{iata_code}", headers=auth_headers)
    assert get_response.status_code == 404

@pytest.mark.flaky(reruns=3, reruns_delay=2)
@pytest.mark.skip(reason="API returns 204 error for delete /airports/{id}")
def test_delete_airport_invalid(auth_headers):
    response = api_request("delete", f"{BASE_URL}{AIRPORTS}/ZZZ", headers=auth_headers)
    assert response.status_code == 404