import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    PAGE_PATH = "admin/login"

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "logButton")
    ERROR_MESSAGE = (By.XPATH, "//h6[normalize-space()='Access Denied']")

    @allure.step("Opening login page")
    def open(self, base_url):
        self.navigate_to(base_url + self.PAGE_PATH) 

    @allure.step("Entering email: {email}")
    def enter_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    @allure.step("Entering password: {password}")
    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)

    @allure.step("Clicking login button")
    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step("Getting error message")
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
