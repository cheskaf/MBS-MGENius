import pytest
import allure
from elements.admin_pages.dashboard_page import DashboardPage
from elements.components.admin_navigation import AdminNavigation

@allure.epic("Admin User Features")
@allure.feature("A2 - Admin Dashboard")
@pytest.mark.admin
class TestAdminDashboard:

    @pytest.fixture(autouse=True)
    def setup(self, logged_in_superadmin, base_url):
        self.dashboard_page = logged_in_superadmin
        self.base_url = base_url
        self.sidebar = AdminNavigation(self.dashboard_page.driver)

    #A2_01
    @allure.story("A2_01 Verify Admin Sidebar and Header)")
    @allure.title("A2_01 - Verify Admin Sidebar and Header")
    @allure.description("""
        This test verifies that the admin dashboard sidebar and header display all expected elements correctly.
        """)
    def test_A2_01(self):
        assert self.sidebar.is_sidebar_displayed(), "Sidebar is not displayed correctly."
        assert self.sidebar.are_sidebar_labels_displayed(), "Not all sidebar labels are displayed."
        assert self.sidebar.are_sidebar_links_displayed(), "Not all sidebar links are displayed."
        assert self.sidebar.are_users_submenu_links_displayed(), "Not all Users submenu links are displayed."