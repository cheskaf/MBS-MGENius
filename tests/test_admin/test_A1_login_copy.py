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
class TestAdminLogin:

    @allure.story("03 - Sign in using Invalid Credentials")
    @allure.title("03 - Sign in using Invalid Credentials")
    @pytest.mark.parametrize("email,password,expected_error", invalid_cases)
    def test_invalid_login(self, driver, base_url, email, password, expected_error):
        login_page = LoginPage(driver)
        
        login_page.open(base_url)
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login()

        assert login_page.get_error_message() == expected_error


    @allure.story("02 - Sign in using Valid Credentials")
    @allure.title("02 - Sign in using Valid Credentials")
    def test_valid_login(self, driver, base_url, superadmin_credentials):
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        login_page.open(base_url)
        login_page.enter_email(superadmin_credentials["email"])
        login_page.enter_password(superadmin_credentials["password"])
        login_page.click_login()

        assert "Welcome" in dashboard_page.get_welcome_banner_text()