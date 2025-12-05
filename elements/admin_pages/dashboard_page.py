import allure
from selenium.webdriver.common.by import By
from elements.base_page import BasePage
from config.urls import ADMIN_DASHBOARD, MODULE_LIST, MODULE_LIST_PENDING, MODULE_LIST_PUBLISHED, MODULE_LIST_UNPUBLISHED, EMPLOYEE_LIST

class DashboardPage(BasePage):
    PAGE_PATH = ADMIN_DASHBOARD
    MODULES_PATH = MODULE_LIST
    MODULES_PENDING_PATH = MODULE_LIST_PENDING
    MODULES_PUBLISHED_PATH = MODULE_LIST_PUBLISHED
    MODULES_UNPUBLISHED_PATH = MODULE_LIST_UNPUBLISHED
    EMPLOYEES_PATH = EMPLOYEE_LIST

    # Page Locators
    WELCOME_BANNER = (By.CSS_SELECTOR, "div[class='hero-inner'] h1")
    
    # Daily Visits
    DAILY_VISITS_CARD = (By.ID, "toggle1")
    DAILY_VISITS_LABEL = (By.XPATH, "//div[@id='toggle1']//div//div[@class='card-stats-title pt-15 pb-15 pl-15 pr-15 letter stats-title-fixed']")
    DAILY_VISITS_DATE = (By.ID, "currentDate")
    DAILY_VISITS_COUNT = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[3]/section[1]/div[2]/div[1]/div[1]/div[1]/div[2]/h1[1]")

    # Expiring Modules
    EXPIRING_MODULES_CARD = (By.ID, "toggle2")
    EXPIRING_MODULES_LABEL = (By.XPATH, "//div[normalize-space()='Employees with Expiring Module']")
    EXPIRING_MODULES_COUNT = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[3]/section[1]/div[2]/div[2]/div[1]/div[1]/div[2]/h1[1]")

    # Modules Statistics
    MODULES_SECTION = (By.XPATH, "//h4[normalize-space()='Modules']")
    TOTAL_MODULES_CARD = (By.XPATH, "//h4[normalize-space()='Total Modules']")
    TOTAL_MODULES_COUNT = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[3]/section[1]/div[2]/div[4]/a[1]/div[1]/div[2]/p[1]")
    PENDING_MODULES_CARD = (By.XPATH, "//h4[normalize-space()='Pending Review Modules']")
    PENDING_MODULES_COUNT = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[3]/section[1]/div[2]/div[5]/a[1]/div[1]/div[2]/p[1]")
    PUBLISHED_MODULES_CARD = (By.XPATH, "//h4[normalize-space()='Published Modules']")
    PUBLISHED_MODULES_COUNT = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[3]/section[1]/div[2]/div[6]/a[1]/div[1]/div[2]/p[1]")
    UNPUBLISHED_MODULES_CARD = (By.XPATH, "//h4[normalize-space()='Unpublished Modules']")
    UNPUBLISHED_MODULES_COUNT = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[3]/section[1]/div[2]/div[7]/a[1]/div[1]/div[2]/p[1]")

    # Employees Statistics
    EMPLOYEES_SECTION = (By.XPATH, "//h4[normalize-space()='Employees']")
    TOTAL_EMPLOYEES_CARD = (By.XPATH, "//h4[normalize-space()='Total Employees Completed Modules']")
    TOTAL_EMPLOYEES_COUNT = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[3]/section[1]/div[2]/div[9]/a[1]/div[1]/div[2]/p[1]")
    COMPLETED_MODULES_CARD = (By.XPATH, "//h4[normalize-space()='Completed Modules Assigned to Employees']")
    COMPLETED_MODULES_COUNT = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[3]/section[1]/div[2]/div[10]/a[1]/div[1]/div[2]/p[1]")
    ACTIVE_EMPLOYEES_CARD = (By.XPATH, "//h4[normalize-space()='Active Employees']")
    ACTIVE_EMPLOYEES_COUNT = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[3]/section[1]/div[2]/div[11]/a[1]/div[1]/div[2]/p[1]")

    # Module Rankings
    MODULE_RANKINGS_SECTION = (By.XPATH, "//h4[contains(text(),'📚 Ranking of Modules')]")
    MODULE_RANKINGS_DESCRIPTION = (By.XPATH, "(//p[@class='mb-0 text-muted'])[1]")
    MODULE_HIGHEST_LABEL = (By.XPATH, "//h5[normalize-space()='Highest']")
    MODULE_LOWEST_LABEL = (By.XPATH, "//h5[normalize-space()='Lowest']")
    MODULE_HIGHEST_ITEM = (By.XPATH, "//div[@class='card']//div[1]//div[1]//div[1]")
    MODULE_LOWEST_ITEM = (By.XPATH, "//div[@class='card-body row']//div[2]//div[1]//div[1]")
    
    # Employee Rankings
    TOP_EMPLOYEES_SECTION = (By.XPATH, "//h4[contains(text(),'🏆 Top Employees')]")
    RANKING_CRITERIA_BUTTON = (By.ID, "toggle3")
    RANK_HEADER = (By.XPATH, "//th[normalize-space()='Rank']")
    EMPLOYEE_NO_HEADER = (By.XPATH, "//th[normalize-space()='No. of Employee']")
    AVERAGE_HEADER = (By.XPATH, "//th[normalize-space()='Average']")
    NO_RANKING_DATA = (By.XPATH, "//b[normalize-space()='Nothing to Display']")

    # Navigation
    @allure.step("Opening dashboard page")
    def open(self, base_url):
        self.navigate_to(base_url + self.PAGE_PATH)
    
    @allure.step("Verifying dashboard page URL ends with expected path")
    def is_at_dashboard_page(self):
        return self.get_current_url().endswith(self.PAGE_PATH)

    @allure.step("Getting welcome banner text")
    def get_welcome_banner_text(self):
        return self.get_text(self.WELCOME_BANNER)
    
    @allure.step("Check if daily visits card is displayed along with its elements")
    def is_daily_visits_card_displayed(self):
        return (self.is_element_displayed(self.DAILY_VISITS_CARD) and
                self.is_element_displayed(self.DAILY_VISITS_LABEL) and
                self.is_element_displayed(self.DAILY_VISITS_DATE) and
                self.is_element_displayed(self.DAILY_VISITS_COUNT))
    
    @allure.step("Check if expiring modules card is displayed along with its elements")
    def is_expiring_modules_card_displayed(self):
        return (self.is_element_displayed(self.EXPIRING_MODULES_CARD) and
                self.is_element_displayed(self.EXPIRING_MODULES_LABEL) and
                self.is_element_displayed(self.EXPIRING_MODULES_COUNT))
    
    @allure.step("Check if modules statistics section is displayed along with its elements")
    def is_modules_statistics_displayed(self):
        return (self.is_element_displayed(self.MODULES_SECTION) and
                self.is_element_displayed(self.TOTAL_MODULES_CARD) and
                self.is_element_displayed(self.TOTAL_MODULES_COUNT) and
                self.is_element_displayed(self.PENDING_MODULES_CARD) and
                self.is_element_displayed(self.PENDING_MODULES_COUNT) and
                self.is_element_displayed(self.PUBLISHED_MODULES_CARD) and
                self.is_element_displayed(self.PUBLISHED_MODULES_COUNT) and
                self.is_element_displayed(self.UNPUBLISHED_MODULES_CARD) and
                self.is_element_displayed(self.UNPUBLISHED_MODULES_COUNT))
    
    @allure.step("Check if employees statistics section is displayed along with its elements")
    def is_employees_statistics_displayed(self):
        return (self.is_element_displayed(self.EMPLOYEES_SECTION) and
                self.is_element_displayed(self.TOTAL_EMPLOYEES_CARD) and
                self.is_element_displayed(self.TOTAL_EMPLOYEES_COUNT) and
                self.is_element_displayed(self.COMPLETED_MODULES_CARD) and
                self.is_element_displayed(self.COMPLETED_MODULES_COUNT) and
                self.is_element_displayed(self.ACTIVE_EMPLOYEES_CARD) and
                self.is_element_displayed(self.ACTIVE_EMPLOYEES_COUNT))
    
    @allure.step("Check if module rankings section is displayed along with its elements")
    def is_module_rankings_displayed(self):
        return (self.is_element_displayed(self.MODULE_RANKINGS_SECTION) and
                self.is_element_displayed(self.MODULE_RANKINGS_DESCRIPTION) and
                self.is_element_displayed(self.MODULE_HIGHEST_LABEL) and
                self.is_element_displayed(self.MODULE_LOWEST_LABEL) and
                self.is_element_displayed(self.MODULE_HIGHEST_ITEM) and
                self.is_element_displayed(self.MODULE_LOWEST_ITEM))
    
    @allure.step("Check if top employees section is displayed along with its elements")
    def is_top_employees_displayed(self):
        return (self.is_element_displayed(self.TOP_EMPLOYEES_SECTION) and
                self.is_element_displayed(self.RANKING_CRITERIA_BUTTON) and
                self.is_element_displayed(self.RANK_HEADER) and
                self.is_element_displayed(self.EMPLOYEE_NO_HEADER) and
                self.is_element_displayed(self.AVERAGE_HEADER))