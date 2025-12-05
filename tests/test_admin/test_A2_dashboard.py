import pytest
import allure
from elements.components.admin_navigation import AdminNavigation

@allure.epic("Admin User Features")
@allure.feature("A2 - Admin Dashboard")
@pytest.mark.admin
class TestAdminDashboard:

    @pytest.fixture(autouse=True)
    def setup(self, logged_in_superadmin, base_url):
        with allure.step("Given the admin is logged in"):
            self.login_page = logged_in_superadmin["login_page"]
            self.dashboard_page = logged_in_superadmin["dashboard_page"]
            self.base_url = base_url
            self.navigation = AdminNavigation(self.dashboard_page.driver)

    #A2_01
    @allure.story("A2_01 Verify Admin Sidebar and Header")
    @allure.title("A2_01 - Verify Admin Sidebar and Header")
    @allure.description("""
        This test verifies that the admin dashboard sidebar and header display all expected elements correctly.
        """)
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_A2_01(self):
        with allure.step("When the admin navigates to the dashboard page"):
            self.dashboard_page.open(self.base_url)
            assert self.dashboard_page.is_at_dashboard_page(), "Not at the dashboard page."
        with allure.step("Then the sidebar and header should display all expected elements correctly"):
            assert self.navigation.is_sidebar_displayed(), "Sidebar is not displayed correctly."
            assert self.navigation.are_sidebar_labels_displayed(), "Not all sidebar labels are displayed."
            assert self.navigation.are_sidebar_links_displayed(), "Not all sidebar links are displayed."
            assert self.navigation.are_users_submenu_links_displayed(), "Not all Users submenu links are displayed."
            assert self.navigation.is_header_displayed(), "Header is not displayed correctly."

    #A2_02
    @allure.story("A2_02 Verify Admin Dashboard Elements")
    @allure.title("A2_02 - Verify Admin Dashboard Elements")
    @allure.description("""
        This test verifies that all key elements on the admin dashboard are displayed correctly.
        """)
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_A2_02(self):
        with allure.step("When the admin navigates to the dashboard page"):
            self.dashboard_page.open(self.base_url)
            assert self.dashboard_page.is_at_dashboard_page(), "Not at the dashboard page."
        with allure.step("Then all key elements on the dashboard should be displayed correctly"):
            assert self.dashboard_page.is_daily_visits_card_displayed(), "Daily Visits card or its elements are not displayed correctly."
            assert self.dashboard_page.is_expiring_modules_card_displayed(), "Expiring Modules card or its elements are not displayed correctly."
            assert self.dashboard_page.is_modules_statistics_displayed(), "Modules Statistics section or its elements are not displayed correctly."
            assert self.dashboard_page.is_employees_statistics_displayed(), "Employees Statistics section or its elements are not displayed correctly."
    
    #A2_03
    @allure.story("A2_03 View Rankings of Modules Section")
    @allure.title("A2_03 - View Rankings of Modules Section")
    @allure.description("""
        This test verifies that the Rankings of Modules section displays correctly with highest and lowest ranked modules.
        """)
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_A2_03(self):
        with allure.step("When the admin navigates to the dashboard page"):
            self.dashboard_page.open(self.base_url)
            assert self.dashboard_page.is_at_dashboard_page(), "Not at the dashboard page."
        with allure.step("Then the Rankings of Modules section should display correctly with highest and lowest ranked modules"):
            assert self.dashboard_page.is_module_rankings_displayed(), "Module Rankings section or its elements are not displayed correctly."

    #A2_04
    @allure.story("A2_04 View Top Employees Section")
    @allure.title("A2_04 - View Top Employees Section")
    @allure.description("""
        This test verifies that the Top Employees section displays correctly with the top-performing employees.
        """)
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_A2_04(self):
        with allure.step("When the admin navigates to the dashboard page"):
            self.dashboard_page.open(self.base_url)
            assert self.dashboard_page.is_at_dashboard_page(), "Not at the dashboard page."
        with allure.step("Then the Top Employees section should display correctly with the top-performing employees"):
            assert self.dashboard_page.is_top_employees_displayed(), "Top Employees section or its elements are not displayed correctly."

    #A2_05
    @allure.story("A2_05 Verify Notification Menu is Displayed Correctly")
    @allure.title("A2_05 - Verify Notification Menu is Displayed Correctly")
    @allure.description("""
        This test verifies that the notification menu in the header displays correctly when clicked.
        """)
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_A2_05(self):
        with allure.step("When the admin navigates to the dashboard page"):
            self.dashboard_page.open(self.base_url)
            assert self.dashboard_page.is_at_dashboard_page(), "Not at the dashboard page."
        with allure.step("And the admin clicks the notification icon in the header"):
            self.navigation.open_notification_dropdown()
        with allure.step("Then the notification menu should display correctly"):
            assert self.navigation.is_notification_dropdown_displayed(), "Notification dropdown is not displayed correctly."

    #A2_06
    @allure.story("A2_06 Verify User Menu is Displayed Correctly")
    @allure.title("A2_06 - Verify User Menu is Displayed Correctly")
    @allure.description("""
        This test verifies that the user menu in the header displays correctly when clicked.
        """)
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_A2_06(self):
        with allure.step("When the admin navigates to the dashboard page"):
            self.dashboard_page.open(self.base_url)
            assert self.dashboard_page.is_at_dashboard_page(), "Not at the dashboard page."
        with allure.step("And the admin clicks the user icon in the header"):
            self.navigation.open_user_dropdown()
        with allure.step("Then the user menu should display correctly"):
            assert self.navigation.is_user_dropdown_displayed(), "User dropdown is not displayed correctly."