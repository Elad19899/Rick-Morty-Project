# google_home_page.py

from selenium.webdriver.common.by import By
from UI_Tests.Pages.base_page import BasePage

class GoogleHomePage(BasePage):
    def open_google_home(self):
        """
        Navigates the browser to the Google homepage.
        """
        self.driver.get("https://www.google.com")

    def search_for_images(self, search_term):
        """
        Conducts an image search for the given term.
        Args:
            search_term (str): The search term for Google images.
        """
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(search_term + " Rick and Morty")  # Add 'Rick and Morty' to focus the search
        search_box.submit()

    def click_on_correct_image(self, character_name):
        """
        Clicks the correct image based on the character name.
        Args:
            character_name (str): The name of the character to search for.
        """
        # Locate and click the first image that matches the character's name
        images = self.driver.find_elements(By.XPATH, f"//img[contains(@alt, '{character_name}')]")
        if images:
            images[0].click()  # Click the first matching image












