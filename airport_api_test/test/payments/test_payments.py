import pytest
from ...utils.api_helpers import api_request

URL = "http://localhost:8000"
PAYMENTS = "/payments"

def test_create_payment_success(auth_headers, payment_data):
    response = api_request("post", URL + PAYMENTS, json=payment_data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["booking_id"] == payment_data["booking_id"]

# Falta booking_id y payment_method
def test_create_payment_invalid(auth_headers):
    data = {"amount": 100}
    response = api_request("post", URL + PAYMENTS, json=data, headers=auth_headers)
    assert response.status_code == 422

def test_get_payment_success(auth_headers, payment_data):
    create_resp = api_request("post", URL + PAYMENTS, json=payment_data, headers=auth_headers)
    payment_id = create_resp.json()["id"]
    response = api_request("get", URL + PAYMENTS + f"/{payment_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["id"] == payment_id

def test_get_payment_not_found(auth_headers):
    response = api_request("get", URL + PAYMENTS + "/noexiste", headers=auth_headers)
    assert response.status_code == 422
