import pytest
import allure
from elements.admin_pages.dashboard_page import DashboardPage

@allure.epic("Admin User Features")
@allure.feature("A1 - Admin Dashboard")
@pytest.mark.admin
class TestAdminDashboard:

    @pytest.fixture(autouse=True) # Automatically use this fixture for all tests in the class
    def setup_pages(self, driver, base_url, superadmin_credentials):
        """
        Runs before every test in this class.
        """
        self.driver = driver
        self.base_url = base_url
        self.login_page = LoginPage(driver)
        self.dashboard_page = DashboardPage(driver)
        self.superadmin_credentials = superadmin_credentials
    
    #A1_01
    @allure.story("01 - View Sign In page")
    @allure.title("01 - View Sign In page")
    def test_sign_in_page_elements(self):
        self.login_page.open(self.base_url)

        assert self.driver.find_element(*self.login_page.MGENIUS_LOGO).is_displayed()
        assert self.login_page.get_page_title() == "MGENIUS"
        assert "Welcome, Admin" in self.login_page.get_welcome_banner_text()
        assert self.login_page.get_login_label_text() == "Log In to your Account"
        assert self.driver.find_element(*self.login_page.EMAIL_INPUT).is_displayed()
        assert self.driver.find_element(*self.login_page.PASSWORD_INPUT).is_displayed()
        assert self.driver.find_element(*self.login_page.TOGGLE_PASSWORD_BUTTON).is_displayed()
        assert self.driver.find_element(*self.login_page.LOGIN_BUTTON).is_displayed()
        assert self.driver.find_element(*self.login_page.LOGIN_WITH_SSO_BUTTON).is_displayed()
    