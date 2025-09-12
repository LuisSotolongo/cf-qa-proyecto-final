import os
import requests
import json
import pytest
from ...utils.reports_utils import save_html_report
from ...utils.settings import AUTH_LOGIN, AUTH_SIGNUP
from faker import Faker
from jsonschema import validate, ValidationError
from ...utils.api_helpers import api_request

fake = Faker()
BASE_URL = os.getenv("BASE_URL")
USER = os.getenv("ADMIN_USER")
PASSWORD = os.getenv("ADMIN_PASSWORD")



# TA-01 - Valida el acceso exitoso y la generación de token
def test_login_exitoso(login_request):
    response = login_request(USER, PASSWORD)
    assert response.status_code == 200
    assert "access_token" in response.json()

# TA-02 - Valida el rechazo de credenciales inválidas
def test_login_fallido(login_request):
    response = login_request("usuario_invalido", "password_invalida")
    assert response.status_code == 401


# TA-03 - Valida el registro único de usuario
def test_signup_exitoso(user_data):
    response = api_request("post", BASE_URL + AUTH_SIGNUP, json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["full_name"] == user_data["full_name"]
    assert data["role"] == "passenger"


# TA-04 - Valida que no se permita el registro con email duplicado
def test_signup_email_existente(create_user):
    payload = {
        "email": create_user["email"],
        "password": fake.password(),
        "full_name": "Admin Duplicado"
    }
    response = api_request("post", BASE_URL + AUTH_SIGNUP, json=payload)
    assert response.status_code in [400, 409, 422]
    assert "detail" in response.json()

# TA-05 - Valida que no se acepten roles inválidos
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_signup_rol_invalido(user_data):
    payload = user_data.copy()
    payload["role"] = "MegaMind"
    response = api_request("post", BASE_URL + AUTH_SIGNUP, json=payload)
    assert response.status_code in [400, 422, 500]
    assert "detail" in response.json()