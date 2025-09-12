import requests
from time import sleep

RENTRIES = 3

def api_request(method, url, **kwargs):
    for i in range(RENTRIES):
        try:
            response = requests.request(method, url, timeout=5, **kwargs)
            if response.status_code < 500 or i == (RENTRIES - 1):
                return response
        except requests.RequestException:
            if i == (RENTRIES - 1):
                raise
        sleep(2 ** i)
