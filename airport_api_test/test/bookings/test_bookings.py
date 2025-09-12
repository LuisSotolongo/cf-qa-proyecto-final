import pytest
import os
from jsonschema import validate, ValidationError
from dotenv import load_dotenv
from ...utils.api_helpers import api_request
from ...utils.settings import BOOKINGS

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

# TA-23 - Valida la creación de reservas con datos válidos
def test_create_booking_success(auth_headers, create_booking):
    booking_id = create_booking
    response = api_request("get", f"{BASE_URL}{BOOKINGS}/{booking_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == booking_id

# TA-24 - Valida que los datos obligatorios sean requeridos
def test_create_booking_invalid(auth_headers):
    data = {"passengers": []}
    response = api_request("post", BASE_URL + BOOKINGS, json=data, headers=auth_headers)
    assert response.status_code == 422
    assert "detail" in response.json()

# TA-25 - Valida la consulta de todas las reservas
def test_get_all_bookings_success(auth_headers):
    response = api_request("get", BASE_URL + BOOKINGS, headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# TA-26 - Valida la consulta de reserva por id
def test_get_booking_success(auth_headers, create_booking):
    booking_id = create_booking
    response = api_request("get", f"{BASE_URL}{BOOKINGS}/{booking_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == booking_id

# TA-27 - Valida el manejo de errores al consultar reserva no existente
def test_get_booking_not_found(auth_headers):
    response = api_request("get", BASE_URL + BOOKINGS + "/noexiste", headers=auth_headers)
    assert response.status_code == 404

# TA-28 - Valida la actualización de datos de reserva
def test_update_booking_success(auth_headers, create_booking):
    booking_id = create_booking
    update_data = {"status": "paid"}
    response = api_request("patch", f"{BASE_URL}{BOOKINGS}/{booking_id}", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["status"] == "paid"

# TA-29 - Valida el manejo de errores al modificar reserva no existente
def test_update_booking_invalid(auth_headers):
    update_data = {"status": "confirmed"}
    response = api_request("patch", BASE_URL + BOOKINGS + "/noexiste", json=update_data, headers=auth_headers)
    assert response.status_code == 404

# TA-30 - Valida el manejo de errores al eliminar reserva no existente
def test_delete_booking_invalid(auth_headers):
    response = api_request("delete", BASE_URL + BOOKINGS + "/noexiste", headers=auth_headers)
    assert response.status_code == 404