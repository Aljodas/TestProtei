import requests

search_url = "https://qwerty/"


# Возвращает кол-во персонажей по их статусу: Dead, Alive, unknown
def count_elements(status1, status2, status3):
    params = {
        "status1": status1,
        "status2": status2,
        "status3": status3
    }
    response = requests.get(url=search_url, params=params)
    result = response.json()

    if response.ok:
        count = result.get("info", {}).get("count", 0)
        return count


# Возвращает имя персонажа
def get_character_name():
    search_name_url = "https://rickandmortyapi.com/api/character/2"
    response = requests.get(url=search_name_url)
    result = response.json()

    if response.ok:
        name = result.get("name")
        return name

# print(get_character_name())


# Возвращает названия нескольких серий
def get_episodes_names():
    search_episode_url = "https://rickandmortyapi.com/api/episode/10,28"
    response = requests.get(url=search_episode_url)
    result = response.json()

    if response.ok:
        names = [episode['name'] for episode in result]
        return names

# print(get_episodes_names())
