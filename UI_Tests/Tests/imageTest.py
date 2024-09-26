import pytest
from selenium import webdriver
from datetime import datetime
import os
import requests
from UI_Tests.Pages.google_home_page import GoogleHomePage
from UI_Tests.Pages.google_image_search_page import GoogleImagesPage


# Function to fetch characters from the Rick and Morty API
def fetch_characters(api_url="https://rickandmortyapi.com/api/character"):
    characters = []
    url = api_url

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            characters.extend(data['results'])
            url = data['info']['next']
        else:
            print(f"Failed to retrieve characters: {response.status_code}")
            break

    return characters


@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_character_images(setup_browser):
    driver = setup_browser

    # Fetch characters from the API
    characters = fetch_characters()

    # Check if at least two characters were fetched
    assert len(characters) >= 2, "Not enough characters fetched from the API."

    # Choose the first two characters
    first_character = characters[0]
    second_character = characters[1]

    first_character_name = first_character['name']
    first_character_id = first_character['id']

    second_character_name = second_character['name']
    second_character_id = second_character['id']

    print(f"Testing with characters: {first_character_name} and {second_character_name}")

    try:
        # Open Google Home Page
        home_page = GoogleHomePage(driver)
        home_page.open_google_home()
        print("Google Home Page opened successfully.")

        # Verify the correct page loaded
        assert "Google" in driver.title, "Google Home Page not loaded."
        print("Verified: Google Home Page loaded correctly.")

        # Step 2: Search for the first character's images
        home_page.search_character_image(first_character_name)
        print(f"Searched for character '{first_character_name}' successfully.")

        # Step 3: Click on the correct image based on the character ID
        home_page.click_on_correct_image(first_character_id)
        print(f"Clicked on the correct image for character ID: {first_character_id}.")

        # Initialize the images page
        images_page = GoogleImagesPage(driver)

        # Ensure images page loaded
        images_page.wait_for_images_to_load()
        print("Images page loaded successfully.")

        # Take screenshot of the first character
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        first_screenshot = f"screenshots/{first_character_name}-{first_character_id}-{timestamp}.png"
        images_page.capture_screenshot(first_screenshot)
        print(f"Screenshot taken and saved at: {first_screenshot}")

        # Verify screenshot exists
        assert os.path.exists(first_screenshot), "Screenshot was not saved successfully."
        print("Verified: Screenshot saved successfully.")

        # Step 4: Search for the second character's images
        home_page.search_character_image(second_character_name)
        print(f"Searched for character '{second_character_name}' successfully.")

        # Click on the correct image for the second character
        home_page.click_on_correct_image(second_character_id)
        print(f"Clicked on the correct image for character ID: {second_character_id}.")

        # Take screenshot of the second character
        second_screenshot = f"screenshots/{second_character_name}-{second_character_id}-{timestamp}.png"
        images_page.capture_screenshot(second_screenshot)
        print(f"Screenshot taken and saved at: {second_screenshot}")

        # Verify screenshot exists
        assert os.path.exists(second_screenshot), "Screenshot was not saved successfully."
        print("Verified: Second screenshot saved successfully.")

        # Step 5: Retrieve and verify character locations (from the UI logic)
        first_character_location = home_page.get_character_location(first_character_name)
        second_character_location = home_page.get_character_location(second_character_name)

        # Verify and assert if the locations are the same or different
        if first_character_location == second_character_location:
            print(f"Both characters are from {first_character_location}.")
        else:
            print(
                f"{first_character_name} is from {first_character_location} and {second_character_name} is from {second_character_location}.")

        # Assert that the locations match
        assert first_character_location == second_character_location, \
            f"{first_character_name} is from {first_character_location} and {second_character_name} is from {second_character_location}."

        print("Test passed: All steps completed successfully.")

    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise


























