# fetch_characters.py

import requests

def fetch_characters():
    """
    Fetches all characters from the Rick and Morty API.
    Returns:
        List of dictionaries, each containing details of a character.
    """
    base_url = 'https://rickandmortyapi.com/api'
    url = f"{base_url}/character"
    characters = []

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            characters.extend(data['results'])  # Append the current page's characters
            url = data['info']['next']  # Move to the next page
        else:
            print(f"Failed to retrieve characters: {response.status_code}")
            break

    return characters



