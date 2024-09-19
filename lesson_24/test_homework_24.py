import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth

@pytest.fixture(scope='class')
def authenticate():
    session = requests.Session()
    url = "http://127.0.0.1:8080/auth"
    auth = HTTPBasicAuth("test_user", "test_pass")
    response = session.post(url, auth=auth)
    assert response.status_code == 200
    token = response.json().get("access_token")
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session


# Налаштування логування
logging.basicConfig(filename='test_search.log', level=logging.INFO, 
format='%(asctime)s - %(levelname)s - %(message)s')


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 1),
        ("price", 5),
        ("year", 5),
        ("year", 10),
        ("engine_volume", 5),
        ("engine_volume", 10),
        ("brand", 5),
    ],
)
def test_search(authenticate, sort_by, limit):
    url = f'http://127.0.0.1:8080/cars?sort_by="{sort_by}"&limit={limit}'
    headers = {
        "Authorization": f"Bearer {authenticate.headers.get('Authorization')}",
        "Accept-Language": "en-gb"
    }
    response = requests.get(url, headers=headers)

    logging.info(f"Testing with sort_by={sort_by} and limit={limit}")
    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response.json()}")

    assert response.status_code == 200
    assert "cars" in response.json()
