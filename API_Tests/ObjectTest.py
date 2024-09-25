import requests
import random

# Base URL of the Rick and Morty API
base_url = 'https://rickandmortyapi.com/api'

# Fetch all episodes (same as before)
url = f"{base_url}/episode"
episodes = []

while url:  # Continue while there's a URL
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        episodes.extend(data['results'])
        url = data['info']['next']  # Update the URL for the next page
    else:
        print(f"Failed to retrieve episodes: {response.status_code}")
        break  # Exit the loop if the request fails

# Filter episodes with 30 or more characters
filtered_episodes = [ep for ep in episodes if len(ep['characters']) >= 30]

if filtered_episodes:
    # Randomly select one episode
    selected_episode = random.choice(filtered_episodes)

    # Randomly select two characters from the chosen episode
    character_urls = selected_episode['characters']
    selected_character_urls = random.sample(character_urls, 2)

    class Character:
        def __init__(self, id, name, status, species, location):
            self.id = id
            self.name = name
            self.status = status
            self.species = species
            self.location = location

    # Fetch character details simultaneously
    responses = [requests.get(url) for url in selected_character_urls]
    characters = []

    for response in responses:
        if response.status_code == 200:
            char_data = response.json()
            character = Character(
                id=char_data['id'],
                name=char_data['name'],
                status=char_data['status'],
                species=char_data['species'],
                location=char_data['location']['name']  # Assuming you want the location name
            )
            characters.append(character)
        else:
            print(f"Failed to retrieve character: {response.status_code}")

    # Step 6: Write introductions to the text file
    with open('characters_introduction.txt', 'w') as f:
        for char in characters:
            introduction = f"Hi! I'm {char.name}, My ID is {char.id}, I'm from {char.location}, etc.\n"
            f.write(introduction)

    print("Introductions written to characters_introduction.txt")
else:
    print("No episodes found with 30 or more characters.")
