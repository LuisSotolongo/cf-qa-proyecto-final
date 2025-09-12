import pytest
import os
import requests
from jsonschema import validate
from dotenv import load_dotenv
from ...utils.api_helpers import api_request
from ...utils.settings import USERS, AUTH_LOGIN, AIRPORTS, FLIGHTS
from datetime import datetime, timedelta

load_dotenv()
BASE_URL = os.getenv("BASE_URL")


def test_create_flight_success(auth_headers, flight_data):
    response = api_request("post", BASE_URL + FLIGHTS, json=flight_data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["origin"] == flight_data["origin"]
# Faltan campos obligatorios
def test_create_flight_invalid(auth_headers):
    data = {"origin": "AAA"}
    response = api_request("post", BASE_URL + FLIGHTS, json=data, headers=auth_headers)
    assert response.status_code == 422

def test_get_flight_success(auth_headers, flight_id):
    response = api_request("get", BASE_URL + FLIGHTS + f"/{flight_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == flight_id

def test_get_flight_not_found(auth_headers):
    response = api_request("get", BASE_URL + FLIGHTS + "/noexiste", headers=auth_headers)
    assert response.status_code in [404 , 422]

def test_search_flights_invalid_params(auth_headers):
    response = api_request("get", BASE_URL + FLIGHTS + "?origin=AAA&date=invalid-date", headers=auth_headers)
    assert response.status_code == 422
