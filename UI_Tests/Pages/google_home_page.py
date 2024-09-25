# In pages/google_home.py
from selenium.webdriver.common.by import By


class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver

    def open_google_home(self):
        self.driver.get("https://www.google.com")

    def search_for_images(self, search_term):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(search_term)
        search_box.submit()

    def search_character_image(self, character_name):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.clear()  # Clear the previous search
        search_box.send_keys(character_name)
        search_box.submit()

    def click_on_correct_image(self, character_id):
        # Implement logic to click the correct image based on character ID
        pass

    def get_character_location(self, character_name):
        # Implement the logic to retrieve the location of the character
        # This is a placeholder and should be replaced with the actual logic
        if character_name == "Rick Sanchez":
            return "Earth"
        elif character_name == "Morty Smith":
            return "Earth"
        return "Unknown"

















