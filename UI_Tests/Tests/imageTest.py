# imageTest.py

import pytest
from selenium import webdriver
from datetime import datetime
import os
import random
from UI_Tests.Pages.google_home_page import GoogleHomePage
from UI_Tests.Pages.google_image_search_page import GoogleImagesPage
from UI_Tests.Pages.fetch_characters import fetch_characters

@pytest.fixture
def setup_browser():
    """
    Sets up the Chrome browser for testing.
    Yields:
        driver (webdriver.Chrome): A Chrome WebDriver instance.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_character_images(setup_browser):
    """
    Test that searches for two random characters from Rick and Morty
    on Google Images and takes screenshots.
    Args:
        setup_browser: PyTest fixture that sets up and tears down the WebDriver.
    """
    driver = setup_browser

    # Step 1: Fetch characters from the API
    characters = fetch_characters()
    print(f"Fetched {len(characters)} characters from the API.")

    # Ensure we have enough characters
    assert len(characters) >= 2, "Not enough characters to test."

    # Randomly select two characters
    first_character = random.choice(characters)
    second_character = random.choice(characters)

    # Ensure they are not the same character
    while first_character['id'] == second_character['id']:
        second_character = random.choice(characters)

    # Print details of the selected characters
    print(f"Character 1: Name = {first_character['name']}, ID = {first_character['id']}")
    print(f"Character 2: Name = {second_character['name']}, ID = {second_character['id']}")

    # Step 2: Open Google Home Page
    home_page = GoogleHomePage(driver)
    home_page.open_google_home()
    print("Google Home Page opened successfully.")

    # Verify that the correct page loaded
    assert "Google" in driver.title, "Google Home Page not loaded."
    print("Verified: Google Home Page loaded correctly.")

    # Step 3: Search for images of the first character, ensuring Rick and Morty context
    home_page.search_for_images(first_character['name'])
    print(f"Searched for images of {first_character['name']}.")

    # Step 4: Click on the correct image for the first character
    home_page.click_on_correct_image(first_character['name'])
    print(f"Clicked on the image for character: {first_character['name']}.")

    # Initialize the images page
    images_page = GoogleImagesPage(driver)

    # Ensure the images page loaded
    images_page.wait_for_images_to_load()
    print("Images page loaded successfully.")

    # Take a screenshot of the first character
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    first_screenshot = f"screenshots/{first_character['name'].replace(' ', '_')}-{first_character['id']}-{timestamp}.png"
    images_page.capture_screenshot(first_screenshot)
    print(f"Screenshot taken and saved at: {first_screenshot}")

    # Verify the screenshot exists
    assert os.path.exists(first_screenshot), "Screenshot was not saved successfully."
    print("Verified: Screenshot saved successfully.")

    # Step 5: Search for images of the second character
    home_page.search_for_images(second_character['name'])
    print(f"Searched for images of {second_character['name']}.")

    # Click on the correct image for the second character
    home_page.click_on_correct_image(second_character['name'])
    print(f"Clicked on the image for character: {second_character['name']}.")

    # Take a screenshot of the second character
    second_screenshot = f"screenshots/{second_character['name'].replace(' ', '_')}-{second_character['id']}-{timestamp}.png"
    images_page.capture_screenshot(second_screenshot)
    print(f"Screenshot taken and saved at: {second_screenshot}")

    # Verify the screenshot exists
    assert os.path.exists(second_screenshot), "Screenshot was not saved successfully."
    print("Verified: Second screenshot saved successfully.")

    print("Test passed: All steps completed successfully.")
























