"""Login helper functions for test automation."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginHelper:
    """Helper class for login operations."""

    # Locators
    USERNAME_INPUT = (By.CSS_SELECTOR, "[data-testid='username-input']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-testid='password-input']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-testid='login-button']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-testid='error-message']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[data-testid='logout-button']")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        """
        Initialize login helper.

        Args:
            driver: WebDriver instance
            timeout: Wait timeout in seconds
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def login(self, username: str, password: str) -> bool:
        """
        Perform login with given credentials.

        Args:
            username: Username to use for login
            password: Password to use for login

        Returns:
            True if login was successful, False otherwise
        """
        try:
            # Wait for and fill username
            username_field = self.wait.until(
                EC.visibility_of_element_located(self.USERNAME_INPUT)
            )
            username_field.clear()
            username_field.send_keys(username)

            # Fill password
            password_field = self.driver.find_element(*self.PASSWORD_INPUT)
            password_field.clear()
            password_field.send_keys(password)

            # Click login button
            login_button = self.driver.find_element(*self.LOGIN_BUTTON)
            login_button.click()

            # Wait for successful login (logout button appears)
            self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BUTTON))
            return True
        except Exception:
            return False

    def logout(self) -> bool:
        """
        Perform logout.

        Returns:
            True if logout was successful, False otherwise
        """
        try:
            logout_button = self.wait.until(
                EC.element_to_be_clickable(self.LOGOUT_BUTTON)
            )
            logout_button.click()
            # Wait for login form to appear
            self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
            return True
        except Exception:
            return False

    def get_error_message(self) -> str:
        """
        Get login error message if present.

        Returns:
            Error message text or empty string if not found
        """
        try:
            error = self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            )
            return error.text
        except Exception:
            return ""

    def is_logged_in(self) -> bool:
        """
        Check if user is currently logged in.

        Returns:
            True if logged in, False otherwise
        """
        try:
            self.driver.find_element(*self.LOGOUT_BUTTON)
            return True
        except Exception:
            return False
