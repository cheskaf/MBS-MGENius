import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    PAGE_PATH = "admin"

    WELCOME_BANNER = (By.CSS_SELECTOR, "div[class='hero-inner'] h1")

    @allure.step("Opening dashboard page")
    def open(self, base_url):
        self.navigate_to(base_url + self.PAGE_PATH)

    @allure.step("Getting welcome banner text")
    def get_welcome_banner_text(self):
        return self.get_text(self.WELCOME_BANNER)
        