import pytest
import os
import time
from dotenv import load_dotenv
from ...utils.api_helpers import api_request
from ...utils.settings import FLIGHTS

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

# TA-17 - Valida la creación de vuelos con datos válidos
def test_create_flight_success(auth_headers, flight_data):
    response = api_request("post", BASE_URL + FLIGHTS, json=flight_data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["origin"] == flight_data["origin"]

# TA-18 - Valida que los datos obligatorios sean requeridos
def test_create_flight_invalid(auth_headers):
    data = {"origin": "AAA"}
    response = api_request("post", BASE_URL + FLIGHTS, json=data, headers=auth_headers)
    assert response.status_code == 422
    assert "detail" in response.json()

# TA-19 - Valida la consulta de vuelo por id
def test_get_flight_success(auth_headers, create_flight):
    flight_id = create_flight
    response = api_request("get", f"{BASE_URL}{FLIGHTS}/{flight_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == flight_id

# TA-20 - Valida el manejo de errores al consultar vuelo no existente
def test_get_flight_not_found(auth_headers):
    response = api_request("get", BASE_URL + FLIGHTS + "/noexiste", headers=auth_headers)
    assert response.status_code == 404

# TA-21 - Valida la restricción de parámetros de búsqueda
def test_search_flights_invalid_params(auth_headers):
    response = api_request("get", BASE_URL + FLIGHTS + "?origin=AAA&date=invalid-date", headers=auth_headers)
    assert response.status_code == 422
    assert "detail" in response.json()

# TA-22 - Valida el rendimiento del endpoint
def test_flight_response_time(auth_headers):
    inicio = time.time()
    response = api_request("get", FLIGHTS, headers=auth_headers)
    fin = time.time()
    assert fin - inicio < 2
    assert response.status_code == 200