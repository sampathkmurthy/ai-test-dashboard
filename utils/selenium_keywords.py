from selenium.webdriver.common.by import By
from utils.retry import retry
from robot.libraries.BuiltIn import BuiltIn

def _get_driver():
    selib = BuiltIn().get_library_instance('SeleniumLibrary')
    return selib.driver

class SeleniumKeywords:
    """Custom Selenium keywords with retry support."""

    print(">>> SeleniumKeywords library loaded")

    @retry(max_attempts=3, delay=2, exceptions=(Exception,))
    def click_element_by_id(self, element_id):
        """Clicks an element by its ID (with retry)."""
        driver = _get_driver()
        if not driver:
            raise RuntimeError("WebDriver is not available. Ensure SeleniumLibrary has opened a browser.")
        driver.find_element(By.ID, element_id).click()

    @retry(max_attempts=3, delay=2, exceptions=(Exception,))
    def enter_text_by_id(self, element_id, text):
        """Enters text into an element by ID (with retry)."""
        driver = _get_driver()
        if not driver:
            raise RuntimeError("WebDriver is not available. Ensure SeleniumLibrary has opened a browser.")
        field = driver.find_element(By.ID, element_id)
        field.clear()
        field.send_keys(text)
