import requests
import os
from dotenv import load_dotenv

load_dotenv()


def fetch_data(animal_name):
    """
    Fetches the animal data for the given 'animal_name'.

    Args:
    - animal_name: The name of the animal to fetch data for.

    Returns:
    - A list of dictionaries, each containing details about an animal.
    """
    api_key = os.getenv('API_KEY')
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": api_key}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Returns a list of animal objects
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return []

