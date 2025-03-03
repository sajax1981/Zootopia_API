import requests
from typing import List, Dict


API_KEY = "hSiV4NgjXtCduOrVXIM1fQ==Xt58CDbBVUcp0I20"
URL = "https://api.api-ninjas.com/v1/animals?name={}"


def fetch_data(animal_name: str) -> List[Dict]:
    """
    Fetches the animal data for the given 'animal_name'.

    Args:
    - animal_name: The name of the animal to fetch data for.

    Returns:
    - A list of dictionaries, each containing details about an animal.
    """
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(URL.format(animal_name), headers=headers)
        response.raise_for_status()


        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

    return []

