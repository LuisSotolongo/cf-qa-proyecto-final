import pytest
import os
from dotenv import load_dotenv
from faker import Faker
from ...utils.settings import USERS, USERS_ME, USERS_LIST, USER_DELETE, USER_UPDATE
from ...utils.api_helpers import api_request

fake = Faker()
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
USER_INVALID_ID = "123456789"

@pytest.fixture
def user_data():
    return {
        "email": fake.unique.email(),
        "password": fake.password(),
        "full_name": fake.name(),
        "role": "admin"
    }

# prueba crear usuario válido
def test_create_user_valid(auth_headers, user_data):
    response = api_request("POST", f"{BASE_URL}{USERS}", json=user_data, headers=auth_headers)
    assert response.status_code == 201
    assert "id" in response.json()

# Prueba sin el campo email
def test_create_user_invalid(auth_headers):
    data = {"username": fake.unique.email(), "password": fake.password()}
    response = api_request("POST", f"{BASE_URL}{USERS}", json=data, headers=auth_headers)
    assert response.status_code in [400, 422]

# prueba lista de usuarios
def test_list_users(auth_headers):
    response = api_request("GET", f"{BASE_URL}{USERS}", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# prueba obtener usuario actual
def test_get_me(auth_headers):
    response = api_request("GET", f"{BASE_URL}{USERS_ME}", headers=auth_headers)
    assert response.status_code == 200
    assert "email" in response.json()

# prueba actualizar usuario
def test_update_user_valid(auth_headers, user_data):
    # Crear usuario
    create_resp = api_request("POST", f"{BASE_URL}{USERS}", json=user_data, headers=auth_headers)
    assert create_resp.status_code == 201, f"Respuesta inesperada: {create_resp.status_code}, {create_resp.text}"
    user_id = create_resp.json()["id"]

    update_data = {
        "email": "luisrodriguezd@email.com",
        "password": user_data["password"],
        "full_name": user_data["full_name"]
    }
    response = api_request("PUT", f"{BASE_URL}{USERS}/{user_id}", json=update_data, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["email"] == "luisrodriguezd@email.com"


# prueba actualizar usuario con id inválido
def test_update_user_invalid(auth_headers):
    response = api_request("PUT", f"{BASE_URL}{USERS}/USER_INVALID_ID", json={"email": "fail@example.com"}, headers=auth_headers)
    assert response.status_code in [404, 400, 422]

# prueba eliminar usuario
def test_delete_user_valid(auth_headers, user_data):
    create_resp = api_request("POST", f"{BASE_URL}{USERS}", json=user_data, headers=auth_headers)
    assert create_resp.status_code == 201, f"Respuesta inesperada: {create_resp.status_code}, {create_resp.text}"
    user_id = create_resp.json()["id"]
    response = api_request("DELETE", f"{BASE_URL}{USERS}/{user_id}", headers=auth_headers)
    assert response.status_code == 204

# prueba eliminar usuario con id inválido da 204 no content
def test_delete_user_invalid(auth_headers):
    response = api_request("DELETE", f"{BASE_URL}{USERS}/USER_INVALID_ID", headers=auth_headers)
    assert response.status_code in [204, 404, 400, 422]
