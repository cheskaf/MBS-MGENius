import pytest
import allure
from pages.admin_pages.login_page import LoginPage
from pages.admin_pages.dashboard_page import DashboardPage

invalid_cases = [
    ("invalid@example.com", "wrongpass", "Access Denied"),
    ("", "", "Access Denied")
]

@allure.epic("Admin User Features")
@allure.feature("A1 - Admin Login")
@pytest.mark.admin
class TestAdminLogin:

    @pytest.fixture(autouse=True)
    def setup_pages(self, driver, base_url, superadmin_credentials):
        """
        Runs before every test in this class.
        """
        self.driver = driver
        self.base_url = base_url
        self.login_page = LoginPage(driver)
        self.dashboard_page = DashboardPage(driver)
        self.superadmin_credentials = superadmin_credentials

    @allure.story("03 - Sign in using Invalid Credentials")
    @allure.title("03 - Sign in using Invalid Credentials")
    @pytest.mark.parametrize("email,password,expected_error", invalid_cases)
    def test_invalid_login(self, email, password, expected_error):
        self.login_page.open(self.base_url)
        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        self.login_page.click_login()

        assert self.login_page.get_error_message() == expected_error


    @allure.story("02 - Sign in using Valid Credentials")
    @allure.title("02 - Sign in using Valid Credentials")
    def test_valid_login(self):
        self.login_page.open(self.base_url)
        self.login_page.enter_email(self.superadmin_credentials["email"])
        self.login_page.enter_password(self.superadmin_credentials["password"])
        self.login_page.click_login()

        assert "Welcome" in self.dashboard_page.get_welcome_banner_text()