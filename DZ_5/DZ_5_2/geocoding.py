import requests

search_url = "https://nominatim.openstreetmap.org/search"


# Находим кол-во магазинов по названию и городу, записываем адреса в файл
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
        with open('addresses.txt', 'w') as file:
            for item in result:
                address = item['display_name'] + ', ' + str(item['place_id']) + ', ' + item['type']
                file.write(address + '\n')
                number_addresses += 1
    return number_addresses


# По данным из файла находим адреса магазинов, считаем кол-во и записываем адреса в файл
def get_shop_name(addresses_file):
    count = 0
    with open(addresses_file, 'r') as file:
        with open('addresses_new.txt', 'w') as f:
            for line in file:
                address_parts = line.split(',')
                house = address_parts[1]
                street = address_parts[2]
                city = address_parts[-6]
                type = address_parts[-1]
                place_id = address_parts[-2]
                amenity = address_parts[0]

                params_get = {
                    "city": city,
                    "street": street + house,
                    "place_id": place_id,
                    "type": type,
                    "amenity": amenity,
                    "format": "json"
                }

                response = requests.get(url=search_url, params=params_get)
                result_2 = response.json()
                if response.ok:
                    for item in result_2:
                        print(item['display_name'])
                        address = item['display_name']
                        f.write(address + '\n')
                        count += 1
    return count

# get_shop_name('addresses.txt')


