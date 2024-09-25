import requests

base_url = 'https://rickandmortyapi.com/api'

# Initialize the URL for the first page
url = f"{base_url}/episode"
episodes = []

while url:
    # Send the request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Add the current page of episodes to the list
        episodes.extend(data['results'])
        # Get the URL for the next page
        url = data['info']['next']
    else:
        print(f"Failed to retrieve episodes: {response.status_code}")
        break

# Output the total number of episodes
print(f"Total episodes fetched: {len(episodes)}")

# Output the list of episodes = 51
print(episodes)

