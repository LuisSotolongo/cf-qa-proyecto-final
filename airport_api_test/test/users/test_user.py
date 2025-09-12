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

# prueba crear usuario válido
# TA-03 Registro único de usuario
def test_create_user_valid(auth_headers, user_data):
    response = api_request("POST", f"{BASE_URL}{USERS}", json=user_data, headers=auth_headers)
    assert response.status_code == 201
    assert "id" in response.json()

# Prueba sin el campo email
# TA-04 Validación de email único
def test_create_user_invalid(auth_headers):
    data = {"username": fake.unique.email(), "password": fake.password()}
    response = api_request("POST", f"{BASE_URL}{USERS}", json=data, headers=auth_headers)
    assert response.status_code in [400, 422]

# glitch a veces devuelve status code 500, de ahi el reruns
# TA-05 Listar usuarios con paginación
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_list_users(auth_headers, skip=0, limit=10):
    response = api_request("GET", f"{BASE_URL}{USERS_LIST}?skip={skip}&limit={limit}", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# TA-06 Obtener detalles del usuario autenticado
def test_get_me(auth_headers):
    response = api_request("GET", f"{BASE_URL}{USERS_ME}", headers=auth_headers)
    assert response.status_code == 200
    assert "email" in response.json()


# TA-07 Actualizar información del usuario
def test_update_user_valid(auth_headers, user_data):
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



# TA-08 Manejo de errores al actualizar usuario inexistente
def test_update_user_invalid(auth_headers):
    response = api_request("PUT", f"{BASE_URL}{USERS}/USER_INVALID_ID", json={"email": "fail@example.com"}, headers=auth_headers)
    assert response.status_code in [404, 400, 422]


# TA-09 Eliminar usuario existente
def test_delete_user_valid(auth_headers, user_data):
    create_resp = api_request("POST", f"{BASE_URL}{USERS}", json=user_data, headers=auth_headers)
    assert create_resp.status_code == 201, f"Respuesta inesperada: {create_resp.status_code}, {create_resp.text}"
    user_id = create_resp.json()["id"]
    response = api_request("DELETE", f"{BASE_URL}{USERS}/{user_id}", headers=auth_headers)
    assert response.status_code == 204


# TA-10 Manejo de errores al eliminar usuario inexistente
def test_delete_user_invalid(auth_headers):
    response = api_request("DELETE", f"{BASE_URL}{USERS}/USER_INVALID_ID", headers=auth_headers)
    assert response.status_code in [204, 404, 400, 422]
