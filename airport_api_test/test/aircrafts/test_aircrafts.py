import pytest
import os
from dotenv import load_dotenv
from ...utils.api_helpers import api_request
from ...utils.settings import AIRCRAFTS
from faker import Faker

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
fake = Faker()

@pytest.fixture
def a_aircraft_data():
    return {
        "tail_number": fake.bothify(text="N#####"),
        "model": fake.random_element(elements=["Boeing 737", "Airbus A320", "Embraer 190"]),
        "capacity": fake.random_int(min=100, max=300)
    }

# TA-31 - Valida la consulta de aeronave por id
@pytest.mark.flaky(reruns=3, reruns_delay=5)
def test_create_aircraft_success(auth_headers, create_aircraft):
    resp = api_request("get", BASE_URL + AIRCRAFTS + f"/{create_aircraft}", headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["id"] == create_aircraft

# TA-32 - Valida que los datos obligatorios sean requeridos
def test_create_aircraft_invalid(auth_headers, a_aircraft_data):
    data = {"model": a_aircraft_data["model"]}
    resp = api_request("post", BASE_URL + AIRCRAFTS, json=data, headers=auth_headers)
    assert resp.status_code == 422
    assert "detail" in resp.json()

# TA-33 - Valida la consulta de aeronave por id
def test_get_aircraft_success(auth_headers, create_aircraft):
    resp = api_request("get", BASE_URL + AIRCRAFTS + f"/{create_aircraft}", headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["id"] == create_aircraft

# TA-34 - Valida el manejo de errores al consultar aeronave no existente
def test_get_aircraft_invalid(auth_headers):
    resp = api_request("get", BASE_URL + AIRCRAFTS + "/noexiste", headers=auth_headers)
    assert resp.status_code == 404

# TA-35 - Valida la actualización de datos de aeronave
def test_update_aircraft_success(auth_headers, create_aircraft):
    update_data = {"tail_number": "N54321", "model": "Airbus A320", "capacity": 150}
    resp = api_request("put", BASE_URL + AIRCRAFTS + f"/{create_aircraft}", json=update_data, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["tail_number"] == "N54321"

# TA-36 - Valida que los datos obligatorios sean requeridos
def test_update_aircraft_invalid(auth_headers, create_aircraft):
    data = {"model": "Airbus A320"}
    resp = api_request("put", BASE_URL + AIRCRAFTS + f"/{create_aircraft}", json=data, headers=auth_headers)
    assert resp.status_code == 422

# TA-37 - Valida la eliminación de aeronave existente
@pytest.mark.flaky(reruns=3, reruns_delay=5)
def test_delete_aircraft_success(auth_headers, create_aircraft):
    resp = api_request("delete", BASE_URL + AIRCRAFTS + f"/{create_aircraft}", headers=auth_headers)
    assert resp.status_code == 204

# TA-38 - Valida el manejo de errores al eliminar aeronave no existente
@pytest.mark.flaky(reruns=3, reruns_delay=5)
# @pytest.mark.skip(reason="API returns 204 error for GET /aircrafts/{id}")
def test_delete_aircraft_invalid(auth_headers):
    resp = api_request("delete", BASE_URL + AIRCRAFTS + "/errornoexiste", headers=auth_headers)
    if resp.status_code == 204:
        pytest.fail("Aunque el aircraft_id no existe la respuesta es 204")
    assert resp.status_code == 422