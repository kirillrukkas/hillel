import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

# Виконання запиту
response = requests.get(url, params=params, verify=False)
data = response.json()

# Перевірка наявності фото
if 'photos' in data:
    photos = data['photos']
else:
    assert False, "No photos are found"

print(photos)

for i, photo in enumerate(photos[:2]):  # Завантажуємо два фото
    img_url = photo['img_src']
    img_data = requests.get(img_url, verify=False).content
    with open(f'mars_photo{i+1}.jpg', 'wb') as handler:
        handler.write(img_data)
        print(f"Фото {i+1} збережено як mars_photo{i+1}.jpg")

