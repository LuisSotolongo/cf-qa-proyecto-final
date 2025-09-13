import requests
import os
from time import sleep
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

RENTRIES = 3
EXPECTED_MSG = '"msg":"Airline API up & running"'

def api_request(method, url, **kwargs):
    if method.upper() == "GET" and url == BASE_URL:
        for _ in range(10):
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200 and EXPECTED_MSG in response.text:
                    break
            except requests.RequestException:
                pass
            sleep(3)
        else:
            raise RuntimeError("La API principal no está lista.")

    for i in range(RENTRIES):
        try:
            response = requests.request(method, url, timeout=5, **kwargs)
            if response.status_code < 500 or i == (RENTRIES - 1):
                return response
        except requests.RequestException:
            if i == (RENTRIES - 1):
                raise
        sleep(2 ** i)
    return None
