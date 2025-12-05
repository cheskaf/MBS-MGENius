import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Navigating to URL: {url}")
    def navigate_to(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            raise Exception(f"Failed to navigate to {url}: {str(e)}")

    @allure.step("Getting current URL")
    def get_current_url(self):
        try:
            self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
            return self.driver.current_url
        except Exception as e:
            raise Exception(f"Failed to get current URL: {str(e)}")

    @allure.step("Clicking element: {locator}")
    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception as e:
            raise Exception(f"Failed to click element {locator}: {str(e)}")

    @allure.step("Sending keys to element: {locator} with input: {text}")
    def send_keys(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except Exception as e:
            raise Exception(f"Failed to send keys to element {locator}: {str(e)}")

    @allure.step("Getting text from element: {locator}")
    def get_text(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).text
        except Exception as e:
            raise Exception(f"Failed to get text from element {locator}: {str(e)}")
    
    @allure.step("Checking if element is displayed: {locator}")
    def is_element_displayed(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False
    
    @allure.step("Waiting for element visibility: {locator}")
    def wait_for_element_visibility(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            raise Exception(f"Failed to wait for element visibility {locator}: {str(e)}")

    @allure.step("Checking if password input is masked: {locator}")
    def is_password_masked(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.get_attribute("type") == "password"
        except Exception as e:
            raise Exception(f"Failed to check if password is masked for element {locator}: {str(e)}")
    
    @allure.step("Checking if password input is unmasked: {locator}")
    def is_password_unmasked(self, locator):    
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.get_attribute("type") == "text"
        except Exception as e:
            raise Exception(f"Failed to check if password is unmasked for element {locator}: {str(e)}")
    
    @allure.step("Checking if element has class '{class_name}': {locator}")
    def has_class(self, locator, class_name):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            classes = element.get_attribute("class").split()
            return class_name in classes
        except Exception as e:
            raise Exception(f"Failed to check if element has class {class_name} for element {locator}: {str(e)}")