import sys
from io import BytesIO
import requests
from PIL import Image

toponim = " ".join(sys.argv[1:])
geocoder_api = "http://geocode-maps.yandex.ru/1.x/"
params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponim,
    "format": "json"
}
response = requests.get(geocoder_api, params=params)
if not response:
    ...
else:
    json_response = response.json()
    coords = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]["Point"]["pos"]
    lon, lat = coords.split(" ")
    delta = "0.005"
    map_params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    api_server = 'http://static-maps.yandex.ru/1.x/'
    response = requests.get(api_server, params=map_params)
    Image.open(BytesIO(response.content)).show()