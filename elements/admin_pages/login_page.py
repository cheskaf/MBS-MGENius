import allure
from selenium.webdriver.common.by import By
from elements.base_page import BasePage
from config.urls import ADMIN_LOGIN

class LoginPage(BasePage):
    # Page Locators
    PAGE_PATH = ADMIN_LOGIN

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
    
    # Navigation
    @allure.step("Opening login page")
    def open(self, base_url):
        self.navigate_to(base_url + self.PAGE_PATH) 

    @allure.step("Verifying login page URL ends with expected path")
    def is_at_login_page(self):
        return self.get_current_url().endswith(self.PAGE_PATH)
        
    # Getters for page elements and texts
    @allure.step("Getting page title")
    def get_page_title(self):
        return self.get_text(self.MGENIUS_TITLE)
    
    @allure.step("Getting welcome banner text")
    def get_welcome_banner_text(self):
        return self.get_text(self.WELCOME_BANNER)
    
    @allure.step("Getting login label text")
    def get_login_label_text(self):
        return self.get_text(self.LOGIN_LABEL)
    
    @allure.step("Checking if the logo is displayed")
    def is_logo_displayed(self):
        return self.is_element_displayed(self.MGENIUS_LOGO)
    
    @allure.step("Checking if email input is displayed")
    def is_email_input_displayed(self):
        return self.is_element_displayed(self.EMAIL_INPUT)
    
    @allure.step("Checking if password input is displayed")
    def is_password_input_displayed(self):
        return self.is_element_displayed(self.PASSWORD_INPUT)
    
    @allure.step("Checking if toggle password button is displayed")
    def is_toggle_password_button_displayed(self):
        return self.is_element_displayed(self.TOGGLE_PASSWORD_BUTTON)
    
    @allure.step("Checking if login button is displayed")
    def is_login_button_displayed(self):
        return self.is_element_displayed(self.LOGIN_BUTTON)
    
    @allure.step("Checking if 'Login with Microsoft' button is displayed")
    def is_login_with_sso_button_displayed(self):
        return self.is_element_displayed(self.LOGIN_WITH_SSO_BUTTON)
    
    @allure.step("Getting error message")
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    # Actions    
    @allure.step("Checking if all expected elements are present on the login page")
    def is_login_page_elements_present(self):
        return (self.is_logo_displayed() and
                self.get_page_title() == "MGENIUS" and
                "Welcome, Admin" in self.get_welcome_banner_text() and
                self.get_login_label_text() == "Log In to your Account" and
                self.is_email_input_displayed() and
                self.is_password_input_displayed() and
                self.is_toggle_password_button_displayed() and
                self.is_login_button_displayed() and
                self.is_login_with_sso_button_displayed())

    @allure.step("Login with email: {email} and password: {password}")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
    
    @allure.step("Login with SSO")
    def login_with_sso(self):
        self.click_login_with_sso()
    
    @allure.step("Entering email: {email}")
    def enter_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    @allure.step("Entering password: {password}")
    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)
    
    @allure.step("Toggling password visibility")
    def toggle_password_visibility(self):
        self.click(self.TOGGLE_PASSWORD_BUTTON)

    @allure.step("Getting password input type")
    def get_password_input_type(self):
        return self.get_element_attribute(self.PASSWORD_INPUT, "type")

    @allure.step("Clicking login button")
    def click_login(self):
        self.click(self.LOGIN_BUTTON)
    
    @allure.step("Clicking 'Login with Microsoft' button")
    def click_login_with_sso(self):
        self.click(self.LOGIN_WITH_SSO_BUTTON)