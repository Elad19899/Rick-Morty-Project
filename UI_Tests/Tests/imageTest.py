import pytest
from selenium import webdriver
from datetime import datetime
import os
from UI_Tests.Pages.google_home_page import GoogleHomePage
from UI_Tests.Pages.google_image_search_page import GoogleImagesPage

@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_character_images(setup_browser):
    driver = setup_browser

    try:
        # Open Google Home Page
        home_page = GoogleHomePage(driver)
        home_page.open_google_home()
        print("Google Home Page opened successfully.")

        # Verify the correct page loaded
        assert "Google" in driver.title, "Google Home Page not loaded."
        print("Verified: Google Home Page loaded correctly.")

        # Step 2: Search for Rick & Morty images
        home_page.search_for_images('Rick & Morty images')
        print("Searched for 'Rick & Morty images' successfully.")

        # Step 3: Search for the first character
        first_character_name = "Rick Sanchez"
        first_character_id = 123  # Example ID

        home_page.search_character_image(first_character_name)
        print(f"Searched for character '{first_character_name}' successfully.")

        # Step 4: Click on the correct image based on the character ID
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

        # Step 5: Search for the second character
        second_character_name = "Morty Smith"
        second_character_id = 456  # Example ID

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

        # Step 6: Retrieve and verify character locations
        first_character_location = home_page.get_character_location(first_character_name)
        second_character_location = home_page.get_character_location(second_character_name)

        # Verify and assert if the locations are the same or different
        if first_character_location == second_character_location:
            print(f"Both characters are from {first_character_location}.")
        else:
            print(f"{first_character_name} is from {first_character_location} and {second_character_name} is from {second_character_location}.")

        # Assert that the locations match
        assert first_character_location == second_character_location, \
            f"{first_character_name} is from {first_character_location} and {second_character_name} is from {second_character_location}."

        print("Test passed: All steps completed successfully.")

    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise


























