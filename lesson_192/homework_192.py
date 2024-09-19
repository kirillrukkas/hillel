

import logging
import requests


logging.info("POST")
url = "http://127.0.0.1:8080/upload"
path_to_file = {"image": open("mars_photo1.jpg", "rb")}
response = requests.post(url, files=path_to_file)

if response.status_code == 201:
    created_data = response.json()
    logging.info(f"Створено дані: {created_data}")
else:
    logging.error(f"Помилка. Статус-код: {response.status_code}, {response.text}")

logging.info("GET")
url = "http://127.0.0.1:8080/image/mars_photo1.jpg"
header = {"Content-Type": "text"}
response = requests.get(url, headers=header)
if response.status_code == 200:
    created_data = response.json()
    logging.info(f"Створено дані: {created_data}")
else:
    logging.error(f"Помилка. Статус-код: {response.status_code}, {response.text}")

logging.info("DELETE")
url = "http://127.0.0.1:8080/delete/mars_photo1.jpg"
response = requests.delete(url)
if response.status_code == 200:
    created_data = response.json()
    logging.info(f"Створено дані: {created_data}")
else:
    logging.error(f"Помилка. Статус-код: {response.status_code}, {response.text}")
