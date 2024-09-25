import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleImagesPage:
    def __init__(self, driver):
        self.driver = driver

    def capture_screenshot(self, filename):
        # Ensure the screenshots directory exists
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')
        # Capture screenshot and save it
        self.driver.save_screenshot(filename)

    def wait_for_images_to_load(self):
        # Wait for images to load (optional step, you can adjust based on page structure)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-q]'))
        )







