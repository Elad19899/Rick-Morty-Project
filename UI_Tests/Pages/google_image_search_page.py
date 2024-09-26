# google_image_search_page.py

import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UI_Tests.Pages.base_page import BasePage

class GoogleImagesPage(BasePage):
    def capture_screenshot(self, filename):
        """
        Captures a screenshot and saves it to the specified file.
        Args:
            filename (str): Path where the screenshot should be saved.
        """
        # Ensure the screenshots directory exists
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')
        # Capture screenshot and save it
        self.driver.save_screenshot(filename)

    def wait_for_images_to_load(self):
        """
        Waits for the images to load on the search results page.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img'))
        )




