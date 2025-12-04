import pytest
import allure
from elements.admin_pages.login_page import LoginPage
from elements.admin_pages.dashboard_page import DashboardPage

invalid_cases = [
    ("invalid@example.com", "wrongpass", "Access Denied"),
    ("invalid@example.com", "", "Access Denied"),
    ("", "wrongpass", "Access Denied"),
    ("", "", "Access Denied"),
]

@allure.epic("Admin User Features")
@allure.feature("A1 - Admin Login")
@pytest.mark.admin
class TestAdminLogin:

    @pytest.fixture(autouse=True) # Automatically use this fixture for all tests in the class
    def setup_pages(self, driver, base_url, superadmin_credentials):
        self.driver = driver
        self.base_url = base_url
        self.login_page = LoginPage(driver)
        self.dashboard_page = DashboardPage(driver)
        self.superadmin_credentials = superadmin_credentials
    
    #A1_01
    @allure.story("A1_01 - View Sign In page")
    @allure.title("A1_01 - View Sign In page")
    @allure.description("""
        This test verifies that the Sign In page loads correctly with all expected elements present.
        """)
    def test_A1_01(self):
        self.login_page.open(self.base_url)
        assert self.login_page.is_at_login_page()
        assert self.login_page.is_login_page_elements_present()
    
    #A1_02
    @allure.story("A1_02 - Sign in using Valid Credentials")
    @allure.title("A1_02 - Sign in using Valid Credentials")
    @allure.description("""
        This test verifies that an admin user can successfully sign in using valid credentials.
        """)
    @pytest.mark.flaky(reruns=2, reruns_delay=5) # Retry failed tests up to 2 times with a 5-second delay
    def test_A1_02(self):
        self.login_page.open(self.base_url)
        assert self.login_page.is_at_login_page()
        self.login_page.enter_email(self.superadmin_credentials["email"])
        self.login_page.enter_password(self.superadmin_credentials["password"])
        self.login_page.click_login()
        assert self.dashboard_page.is_at_dashboard_page()
        assert "Welcome" in self.dashboard_page.get_welcome_banner_text()

    #A1_03
    @allure.story("A1_03 - Sign in using Invalid Credentials")
    @allure.title("A1_03 - Sign in using Invalid Credentials")
    @allure.description("""
        This test verifies that appropriate error messages are displayed when signing in with invalid credentials.
        """)
    @pytest.mark.flaky(reruns=2, reruns_delay=5) # Retry failed tests up to 2 times with a 5-second delay
    @pytest.mark.parametrize("email,password,expected_error", invalid_cases)
    def test_A1_03(self, email, password, expected_error):
        self.login_page.open(self.base_url)
        assert self.login_page.is_at_login_page()
        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        self.login_page.click_login()
        assert self.login_page.is_at_login_page()
        assert self.login_page.get_error_message() == expected_error

    #A1_04
    @allure.story("A1_04 - Toggle Password Visibility")
    @allure.title("A1_04 - Toggle Password Visibility")
    @allure.description("""
        This test verifies that the password visibility toggle functions correctly on the login page.
        """)
    def test_A1_04(self):
        self.login_page.open(self.base_url)
        assert self.login_page.is_at_login_page()
        self.login_page.enter_email(invalid_cases[0][0])
        self.login_page.enter_password(invalid_cases[0][1])
        self.login_page.toggle_password_visibility()