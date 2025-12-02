from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_current_url(self):
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        return self.driver.current_url

    def navigate_to(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def wait_for_element_visibility(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def is_password_masked(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute("type") == "password"
    
    def is_password_unmasked(self, locator):    
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute("type") == "text"