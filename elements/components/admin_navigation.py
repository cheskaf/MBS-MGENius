import allure
from selenium.webdriver.common.by import By
from elements.base_page import BasePage
from elements.admin_pages.login_page import LoginPage
from config.urls import LANDING_PAGE, ADMIN_DASHBOARD, MODULE_LIST, CATEGORY_LIST, ADMIN_LIST, EMPLOYEE_LIST, TRAINER_LIST, CREATE_USER, USER_ROLES, GROUP_LIST, NOTIFICATIONS_RECEIVED, ADMIN_LOGOUT

class AdminNavigation(BasePage):
    # Sidebar Locators
    SIDEBAR = (By.ID, "sidebar-wrapper")
    SIDEBAR_LOGO = (By.XPATH, "//img[@alt='Logo']")
    SIDEBAR_TITLE = (By.XPATH, "//a[normalize-space()='MGenius - LMS']")
    LANDING_PATH = LANDING_PAGE

    DASHBOARD = (By.LINK_TEXT, "Dashboard")
    DASHBOARD_PATH = ADMIN_DASHBOARD

    TRAINING_LABEL = (By.XPATH, "//li[normalize-space()='Training']")
    MODULES = (By.LINK_TEXT, "Modules")
    MODULES_PATH = MODULE_LIST

    CATEGORIES_LABEL = (By.XPATH, "//li[contains(text(),'Categories')]")
    CATEGORIES = (By.LINK_TEXT, "Categories")
    CATEGORIES_PATH = CATEGORY_LIST

    USERS_LABEL = (By.XPATH, "//li[normalize-space()='Users']")
    USERS_TOGGLE = (By.XPATH, "//span[normalize-space()='Users']")
    ADMIN_USERS = (By.XPATH, "//a[normalize-space()='Admin']")
    ADMIN_USERS_PATH = ADMIN_LIST
    EMPLOYEE_USERS = (By.XPATH, "//a[normalize-space()='Employees']")
    EMPLOYEE_USERS_PATH = EMPLOYEE_LIST
    TRAINER_USERS = (By.XPATH, "//a[normalize-space()='Trainers']")
    TRAINER_USERS_PATH = TRAINER_LIST
    NEW_USER = (By.XPATH, "//a[normalize-space()='New']")
    NEW_USER_PATH = CREATE_USER
    USER_ROLES_LINK = (By.XPATH, "//span[normalize-space()='User Roles']")
    USER_ROLES_PATH = USER_ROLES

    GROUPS_LABEL = (By.XPATH, "//li[normalize-space()='Groups']")
    GROUPS = (By.XPATH, "//body/div[@id='app']/div[@class='main-wrapper']/div[@class='main-sidebar']/aside[@id='sidebar-wrapper']/ul[@class='sidebar-menu']/li[1]/a[1]")
    GROUPS_PATH = GROUP_LIST

    NOTIF_LABEL = (By.XPATH, "//li[contains(text(),'Notifications')]")
    SENT_NOTIF = (By.XPATH, "//span[normalize-space()='Notifications']")
    SENT_NOTIF_PATH = NOTIFICATIONS_RECEIVED

    LOGOUT_LABEL = (By.XPATH, "//li[normalize-space()='Log Out']")
    SIDEBAR_LOGOUT = (By.XPATH, "//span[normalize-space()='Logout']")
    ADMIN_LOGOUT_PATH = ADMIN_LOGOUT

    # Header Locators
    HEADER = (By.XPATH, "//nav[@class='navbar navbar-expand-lg main-navbar']")
    SIDEBAR_TOGGLE = (By.XPATH, "//i[@class='fas fa-bars']")
    NOTIF_ICON = (By.XPATH, "//i[@class='far fa-bell']")
    NOTIFS_DROPDOWN = (By.XPATH, "//a[@class='nav-link notification-toggle nav-link-lg']")
    NOTIF_MENU = (By.XPATH, "//div[@class='dropdown-menu dropdown-list dropdown-menu-right show']")
    NOTIF_MENU_LABEL = (By.XPATH, "//div[@class='dropdown-header']")
    NOTIF_MENU_NO_DATA = (By.XPATH, "//b[normalize-space()='No Unread Notification']")
    NOTIF_VIEW_ALL = (By.XPATH, "//a[normalize-space()='View All Notifications']")

    HEADER_ICON = (By.XPATH, "//img[@alt='image']")
    HEADER_USER_DROPDOWN = (By.XPATH, "//div[@class='d-sm-none d-lg-inline-block']")
    HEADER_USER_MENU = (By.XPATH, "//div[@class='dropdown-menu dropdown-menu-right show']")
    CHANGE_PASSWORD = (By.XPATH, "//a[normalize-space()='Change Password']")
    SEND_TO_OUTLOOK = (By.ID, "sendToOutlookBtn")
    HEADER_LOGOUT = (By.XPATH, "//a[@class='dropdown-item has-icon text-danger']")

    
    @allure.step("Verifying sidebar is displayed correctly")
    def is_sidebar_displayed(self):
        return (self.is_element_displayed(self.SIDEBAR) and
                self.is_element_displayed(self.SIDEBAR_LOGO) and
                self.is_element_displayed(self.SIDEBAR_TITLE) and
                self.is_element_displayed(self.SIDEBAR_TOGGLE))
    
    @allure.step("Verifying all sidebar labels are displayed")
    def are_sidebar_labels_displayed(self):
        labels = [self.TRAINING_LABEL, self.CATEGORIES_LABEL, self.USERS_LABEL,
                self.GROUPS_LABEL, self.NOTIF_LABEL, self.LOGOUT_LABEL]
        return all(self.is_element_displayed(label) for label in labels)
    
    @allure.step("Verifying all sidebar links are displayed")
    def are_sidebar_links_displayed(self):
        links = [self.DASHBOARD, self.MODULES, self.CATEGORIES,
                self.USERS_TOGGLE, self.USER_ROLES_LINK, self.GROUPS,
                self.SENT_NOTIF, self.SIDEBAR_LOGOUT]
        return all(self.is_element_displayed(link) for link in links)
    
    @allure.step("Verifying all Users submenu links are displayed")
    def are_users_submenu_links_displayed(self):
        if not self.is_element_displayed(self.ADMIN_USERS):
            self.click(self.USERS_TOGGLE)
        user_links = [self.ADMIN_USERS, self.EMPLOYEE_USERS, self.TRAINER_USERS, self.NEW_USER]
        return all(self.is_element_displayed(link) for link in user_links)
    
    @allure.step("Navigating to Landing Page via sidebar title")
    def click_landing_page(self):
        self.click(self.SIDEBAR_TITLE)
    
    @allure.step("Verifying Dashboard link functionality")
    def click_dashboard(self):
        self.click(self.DASHBOARD)
    
    @allure.step("Verifying Modules link functionality")
    def click_modules(self):
        self.click(self.MODULES)
    
    @allure.step("Verifying Categories link functionality")
    def click_categories(self):
        self.click(self.CATEGORIES)
    
    @allure.step("Verifying Admin List link functionality")
    def click_admin_list(self):
        if not self.is_element_displayed(self.ADMIN_USERS):
            self.click(self.USERS_TOGGLE)
        self.click(self.ADMIN_USERS)
    
    @allure.step("Verifying Employee List link functionality")
    def click_employee_list(self):
        if not self.is_element_displayed(self.EMPLOYEE_USERS):
            self.click(self.USERS_TOGGLE)
        self.click(self.EMPLOYEE_USERS)
    
    @allure.step("Verifying Trainer List link functionality")
    def click_trainer_list(self):
        if not self.is_element_displayed(self.TRAINER_USERS):
            self.click(self.USERS_TOGGLE)
        self.click(self.TRAINER_USERS)

    @allure.step("Verifying Create New User link functionality")
    def click_create_user(self):
        if not self.is_element_displayed(self.NEW_USER):
            self.click(self.USERS_TOGGLE)
        self.click(self.NEW_USER)

    @allure.step("Verifying User Roles link functionality")
    def click_user_roles(self):
        self.click(self.USER_ROLES_LINK)
    
    @allure.step("Verifying Groups link functionality")
    def click_groups(self):
        self.click(self.GROUPS)
    
    @allure.step("Verifying Sent Notifications link functionality")
    def click_sent_notifications(self):
        self.click(self.SENT_NOTIF)
    
    @allure.step("Verifying Logout functionality via sidebar")
    def click_logout(self):
        self.click(self.SIDEBAR_LOGOUT)