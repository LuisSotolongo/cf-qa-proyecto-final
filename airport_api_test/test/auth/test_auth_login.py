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






