import requests


address = "Красная Площадь"
link = (f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={address}&format=json")
result = requests.get(link).json()
print(result)

