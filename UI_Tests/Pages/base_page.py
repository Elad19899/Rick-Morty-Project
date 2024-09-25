# base_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=20):  # Increased timeout for stability
        """Wait for an element to be present on the page."""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def wait_for_element_to_be_clickable(self, by, value, timeout=20):
        """Wait for an element to be clickable on the page."""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))












