import os
import requests
from ...utils.settings import AUTH_LOGIN

def login(username, password):
    url = os.getenv("BASE_URL")
    response = requests.post(
        url + AUTH_LOGIN, data={"username": username, "password": password}, timeout=5)
    return response

# Caso positivo: login con credenciales válidas devuelve 200 y token.
# TA-01 Login exitoso
def test_login_exitoso():
    user = os.getenv("ADMIN_USER")
    password = os.getenv("ADMIN_PASSWORD")
    response = login(user, password)
    assert response.status_code == 200
    assert "access_token" in response.json()

# Caso negativo: login con credenciales inválidas devuelve 401.
# TA-02 Login fallido
def test_login_fallido():
    response = login("usuario_invalido", "password_invalida")
    assert response.status_code == 401

# Prueba de registro exitoso

def test_signup_exitoso():
    url = os.getenv("BASE_URL")
    payload = {
        "email": fake.unique.email(),
        "password": fake.password(),
        "full_name": fake.name()
    }
    response = requests.post(url + "/auth/signup", json=payload, timeout=5)
    assert response.status_code == 201
    data = response.json()
    with open('airport_api_test/api_clients/json_schemas/user_create_schema.json') as f:
        schema = json.load(f)
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        assert False, f"Error de validación: {e.message}"
    assert data["email"] == payload["email"]
    assert data["full_name"] == payload["full_name"]
    assert data["role"] == "passenger"


# prueba de registro con email ya existente, Roles permitidos passenger, admin.
def test_signup_email_existente():
    user = os.getenv("ADMIN_USER")
    password = os.getenv("ADMIN_PASSWORD")
    url = os.getenv("BASE_URL")
    payload = {
        "email": user,
        "password": fake.password(),
        "full_name": "Admin Duplicado"
    }
    response = requests.post(url + "/auth/signup", json=payload, timeout=5)
    assert response.status_code in [400, 409, 422]
    print(response.json())
    assert "detail" in response.json()


# prueba de registro con rol inválido detectado glitch en la respuesta
def test_signup_rol_invalido():
    url = os.getenv("BASE_URL")
    payload = {
        "email": fake.unique.email(),
        "password": fake.password(),
        "full_name": "Usuario MegaMind Invalido",
        "role": "MegaMind"
    }
    response = requests.post(url + "/auth/signup", json=payload, timeout=5)
    resp_json = response.json()
    if response.status_code == 201:
        save_html_report(
            "airport_api_test/reports/html_reports/glitch_signup_rol_invalido.html",
            "GLITCH: status 201 con rol inválido",
            payload,
            resp_json
        )
        pytest.fail("GLITCH: La API aceptó un rol inválido y devolvió 201. Ver glitch_signup_rol_invalido.html y .json")
    assert response.status_code in [400, 422, 500]
    assert "detail" in resp_json





