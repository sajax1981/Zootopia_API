import requests
from typing import List, Dict


def fetch_data(animal_name: str) -> List[Dict]:

    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    api_key = "hSiV4NgjXtCduOrVXIM1fQ==Xt58CDbBVUcp0I20"

    headers = {"X-Api-Key": api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Return the animal data as a list of dictionaries
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")

    return []  # Return an empty list in case of an error

