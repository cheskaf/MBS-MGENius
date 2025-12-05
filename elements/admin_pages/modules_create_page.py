import allure
from selenium.webdriver.common.by import By
from elements.base_page import BasePage
from config.urls import MODULE_CREATE

class ModulesCreatePage(BasePage):
    PAGE_PATH = MODULE_CREATE

    # Page Locators
    PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Modules List']")
    BREADCRUMBS = (By.CLASS_NAME, "section-header-breadcrumb")

    # Navigation
    @allure.step("Opening create module page")
    def open(self, base_url):
        self.navigate_to(base_url + self.PAGE_PATH)

    @allure.step("Verifying create module page URL ends with expected path")
    def is_at_create_module_page(self):
        return self.get_current_url().endswith(self.PAGE_PATH)
    
    @allure.step("Getting page title")
    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)