# base_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=20):
        """
        Waits for an element to be present on the page.
        Args:
            by (selenium.webdriver.common.by.By): The type of locator.
            value (str): The value of the locator.
            timeout (int): How long to wait for the element.
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def wait_for_element_to_be_clickable(self, by, value, timeout=20):
        """
        Waits for an element to be clickable.
        """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))









