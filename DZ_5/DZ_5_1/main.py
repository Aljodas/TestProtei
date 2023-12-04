import requests

search_url = "https://rickandmortyapi.com/api/character/"


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
