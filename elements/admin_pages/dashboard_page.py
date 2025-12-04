import allure
from selenium.webdriver.common.by import By
from elements.base_page import BasePage
from config.urls import ADMIN_DASHBOARD

class DashboardPage(BasePage):
    PAGE_PATH = ADMIN_DASHBOARD

    WELCOME_BANNER = (By.CSS_SELECTOR, "div[class='hero-inner'] h1")

    @allure.step("Opening dashboard page")
    def open(self, base_url):
        self.navigate_to(base_url + self.PAGE_PATH)
    
    @allure.step("Verifying dashboard page URL ends with expected path")
    def is_at_dashboard_page(self):
        return self.get_current_url().endswith(self.PAGE_PATH)

    @allure.step("Getting welcome banner text")
    def get_welcome_banner_text(self):
        return self.get_text(self.WELCOME_BANNER)
        