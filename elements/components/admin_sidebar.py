# admin_sidebar.py
import allure
from selenium.webdriver.common.by import By
from elements.base_page import BasePage

class AdminSidebar(BasePage):
    SIDEBAR_LOGO = (By.CLASS_NAME, "sidebar-logo")
    SIDEBAR_TITLE = (By.CLASS_NAME, "sidebar-title")
    
    DASHBOARD_LINK = (By.LINK_TEXT, "Dashboard")
    USERS_LINK = (By.LINK_TEXT, "Users")
    SETTINGS_LINK = (By.LINK_TEXT, "Settings")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")

    @allure.step("Navigating to Dashboard")
    def go_to_dashboard(self):
        self.click(self.DASHBOARD_LINK)

    @allure.step("Navigating to Users")
    def go_to_users(self):
        self.click(self.USERS_LINK)

    @allure.step("Navigating to Settings")
    def go_to_settings(self):
        self.click(self.SETTINGS_LINK)

    @allure.step("Logging out")
    def logout(self):
        self.click(self.LOGOUT_BUTTON)