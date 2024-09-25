import requests
import random

# Base URL of the Rick and Morty API
base_url = 'https://rickandmortyapi.com/api'

# Initialize the URL for the first page of episodes
url = f"{base_url}/episode"
episodes = []

# Fetch all episodes
while url:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        episodes.extend(data['results'])
        url = data['info']['next']
    else:
        print(f"Failed to retrieve episodes: {response.status_code}")
        break

# Filter episodes with 30 or more characters
filtered_episodes = [ep for ep in episodes if len(ep['characters']) >= 30]

# Check if any episodes meet the criteria
if filtered_episodes:
    # Randomly select one episode from the filtered list
    selected_episode = random.choice(filtered_episodes)

    # Print the name of the selected episode and the number of characters
    print(f"Selected Episode: {selected_episode['name']}")
    print(f"Number of Characters: {len(selected_episode['characters'])}")
else:
    print("No episodes found with 30 or more characters.")
