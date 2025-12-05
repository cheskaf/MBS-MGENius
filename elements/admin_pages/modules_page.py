import allure
from selenium.webdriver.common.by import By
from elements.base_page import BasePage
from config.urls import MODULE_LIST

class ModulesPage(BasePage):
    PAGE_PATH = MODULE_LIST

    # Page Locators
    PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Modules List']")
    BREADCRUMBS = (By.CLASS_NAME, "section-header-breadcrumb")
    CREATE_MODULE_BUTTON = (By.ID, "createModuleBtn")
    SEARCH_INPUT = (By.ID, "searchModuleInput")

    # Module Filters
    TOTAL_MODULES_CARD = (By.ID, "totalModules")
    TOTAL_MODULES_COUNT = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[3]/section[1]/div[2]/div[1]/div[1]/div[1]/div[2]/h1[1]")
    PENDING_REVIEW_CARD = (By.ID, "pendingReviewModules")
    PENDING_REVIEW_COUNT = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[3]/section[1]/div[2]/div[2]/div[1]/div[1]/div[2]/h1[1]")
    PUBLISHED_MODULES_CARD = (By.ID, "publishedModules")
    PUBLISHED_MODULES_COUNT = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[3]/section[1]/div[2]/div[3]/div[1]/div[1]/div[2]/h1[1]")
    UNPUBLISHED_MODULES_CARD = (By.ID, "unpublishedModules")
    UNPUBLISHED_MODULES_COUNT = (By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[3]/section[1]/div[2]/div[4]/div[1]/div[1]/div[2]/h1[1]")

    # Module List Table
    TABLE = (By.XPATH, "//table[@id='modulesTable']")
    # Column Headers
    HEADER_TITLE = (By.XPATH, "//th[normalize-space()='Module Name']")
    HEADER_CATEGORY = (By.XPATH, "//th[normalize-space()='Category']")
    HEADER_TRAINER = (By.XPATH, "//th[normalize-space()='Trainer']")
    HEADER_EMPLOYEES = (By.XPATH, "//th[normalize-space()='No. of Employees']")
    HEADER_QUIZ = (By.XPATH, "//th[normalize-space()='No. of Quiz']")
    HEADER_CREATED_AT = (By.XPATH, "//th[normalize-space()='Created At']")
    HEADER_UPDATED_AT = (By.XPATH, "//th[normalize-space()='Updated At']")
    HEADER_STATUS = (By.XPATH, "//th[normalize-space()='Status']")
    HEADER_ACTIONS = (By.XPATH, "//th[normalize-space()='Actions']")

    # Module List Rows and Values
    MODULE_ROW = (By.XPATH, "//table[@id='modulesTable']/tbody/tr")
    ROW_TITLE = (By.XPATH, "//table[@id='modulesTable']/tbody/tr[1]/td[1]")
    ROW_CATEGORY = (By.XPATH, "//table[@id='modulesTable']/tbody/tr[1]/td[2]")
    ROW_TRAINER = (By.XPATH, "//table[@id='modulesTable']/tbody/tr[1]/td[3]")
    ROW_EMPLOYEES = (By.XPATH, "//table[@id='modulesTable']/tbody/tr[1]/td[4]")
    ROW_QUIZ = (By.XPATH, "//table[@id='modulesTable']/tbody/tr[1]/td[5]")
    ROW_CREATED_AT = (By.XPATH, "//table[@id='modulesTable']/tbody/tr[1]/td[6]")
    ROW_UPDATED_AT = (By.XPATH, "//table[@id='modulesTable']/tbody/tr[1]/td[7]")
    ROW_STATUS = (By.XPATH, "//table[@id='modulesTable']/tbody/tr[1]/td[8]")
    ROW_ACTIONS = (By.XPATH, "//table[@id='modulesTable']/tbody/tr[1]/td[9]")

    # Actions Menu
    MODULE_PUBLISH_OPTION = (By.XPATH, "//a[normalize-space()='Publish/Unpublish']")
    MODULE_EDIT_OPTION = (By.XPATH, "//a[normalize-space()='Edit Module']")
    MODULE_EMPLOYEES_OPTION = (By.XPATH, "//a[normalize-space()='Module Employees']")
    MODULE_QUIZZES_OPTION = (By.XPATH, "//a[normalize-space()='Module Quizzes']")
    MODULE_FORUMS_OPTION = (By.XPATH, "//a[normalize-space()='Module Forums']")
    MODULE_PREVIEW_OPTION = (By.XPATH, "//a[normalize-space()='Preview Module']")
    MODULE_DELETE_OPTION = (By.XPATH, "//a[normalize-space()='Delete Module']")

    # Pagination
    PREVIOUS_BUTTON = (By.ID, "modulesTable_previous")
    NEXT_BUTTON = (By.ID, "modulesTable_next")
    PAGE_ONE_BUTTON = (By.XPATH, "//a[normalize-space()='1']")

    # Navigation
    @allure.step("Opening modules page")
    def open(self, base_url):
        self.navigate_to(base_url + self.PAGE_PATH)

    @allure.step("Verifying modules page URL ends with expected path")
    def is_at_modules_page(self):
        return self.get_current_url().endswith(self.PAGE_PATH)
    
    @allure.step("Getting page title")
    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)
    
    @allure.step("Checking if Create Module button is displayed")
    def is_create_module_button_displayed(self):
        return self.is_element_displayed(self.CREATE_MODULE_BUTTON)
    
    # Actions
    @allure.step("Clicking Create Module button")
    def click_create_module_button(self):
        self.click(self.CREATE_MODULE_BUTTON)