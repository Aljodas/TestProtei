import requests

search_url = "https://nominatim.openstreetmap.org/search"


def search_addresses(city, amenity):
    params_search = {
        "city": city,
        "amenity": amenity,
        "format": "json"
    }

    response = requests.get(url=search_url, params=params_search)
    result = response.json()

    number_addresses = 0
    if response.ok:
        with open('addresses.txt', 'w', encoding='utf-8') as file:
            for item in result:
                address = item['display_name']
                file.write(address + '\n')
                number_addresses += 1
    return number_addresses


class GeocodingMock:
    def search_addresses(self, city, amenity):
        return [{"display_name": "Магазин 1"}, {"display_name": "Магазин 2"}, {"display_name": "Магазин 3"}]

