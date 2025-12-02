import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    PAGE_PATH = "admin/login"

    MGENIUS_LOGO = (By.CLASS_NAME, "myimg")
    MGENIUS_TITLE = (By.XPATH, "//h1[normalize-space()='MGENIUS']")
    WELCOME_BANNER = (By.XPATH, "//h3[1]")
    LOGIN_LABEL = (By.XPATH, "//p[normalize-space()='Log In to your Account']")

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    TOGGLE_PASSWORD_BUTTON = (By.ID, "togglePassword")
    
    LOGIN_BUTTON = (By.CLASS_NAME, "logButton")
    LOGIN_WITH_SSO_BUTTON = (By.XPATH, "//button[normalize-space()='Login with Microsoft']")
    
    ERROR_MESSAGE = (By.XPATH, "//h6[normalize-space()='Access Denied']")


    @allure.step("Opening login page")
    def open(self, base_url):
        self.navigate_to(base_url + self.PAGE_PATH) 
    
    @allure.step("Getting page title")
    def get_page_title(self):
        return self.get_text(self.MGENIUS_TITLE)
    
    @allure.step("Getting welcome banner text")
    def get_welcome_banner_text(self):
        return self.get_text(self.WELCOME_BANNER)
    
    @allure.step("Getting login label text")
    def get_login_label_text(self):
        return self.get_text(self.LOGIN_LABEL)
    
    @allure.step("Entering email: {email}")
    def enter_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    @allure.step("Entering password: {password}")
    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)
    
    @allure.step("Toggling password visibility")
    def toggle_password_visibility(self):
        self.is_password_masked(self.PASSWORD_INPUT)  # Check if masked before toggling
        self.click(self.TOGGLE_PASSWORD_BUTTON)
        self.is_password_unmasked(self.PASSWORD_INPUT)  # Check if unmasked after toggling

    @allure.step("Clicking login button")
    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step("Getting error message")
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
