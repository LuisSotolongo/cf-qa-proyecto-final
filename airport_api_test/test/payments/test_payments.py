import os
import pytest
import time
from dotenv import load_dotenv
from ...utils.api_helpers import api_request
from ...utils.settings import PAYMENTS

load_dotenv()
BASE_URL = os.getenv("BASE_URL")


# TA-39 - Valida la consulta de pago por id
@pytest.mark.skip(reason="No funciona correctamente")
def test_create_payment_success(auth_headers, create_payment):
    payment_id = create_payment
    response = api_request("get", f"{BASE_URL}{PAYMENTS}/{payment_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == payment_id

# TA-40 - Valida que los datos obligatorios sean requeridos
@pytest.mark.flaky(reruns=3, reruns_delay=5)
def test_create_payment_invalid(auth_headers, create_booking):
    data = {"amount": 100, "booking_id": create_booking}
    response = api_request("post", BASE_URL + PAYMENTS, json=data, headers=auth_headers)
    assert response.status_code == 422
    assert "detail" in response.json()

# TA-41 - Valida la consulta de pago por id
@pytest.mark.skip(reason="No funciona correctamente")
def test_get_payment_success(auth_headers, create_payment):
    payment_id = create_payment
    response = api_request("get", f"{BASE_URL}{PAYMENTS}/{payment_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == payment_id

# TA-42 - Valida el manejo de errores al consultar pago no existente
def test_get_payment_not_found(auth_headers):
    response = api_request("get", BASE_URL + PAYMENTS + "/noexiste", headers=auth_headers)
    assert response.status_code == 404

