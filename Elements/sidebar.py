"""Sidebar page object class for interacting with sidebar elements."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Sidebar:
    """Page object class for sidebar interactions."""

    # Locators
    SIDEBAR_CONTAINER = (By.CSS_SELECTOR, "[data-testid='sidebar']")
    MENU_ITEMS = (By.CSS_SELECTOR, "[data-testid='sidebar'] .menu-item")
    TOGGLE_BUTTON = (By.CSS_SELECTOR, "[data-testid='sidebar-toggle']")
    COLLAPSE_BUTTON = (By.CSS_SELECTOR, "[data-testid='sidebar-collapse']")

    def __init__(self, driver: WebDriver, timeout: int = 10):
        """
        Initialize sidebar page object.

        Args:
            driver: WebDriver instance
            timeout: Wait timeout in seconds
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def is_visible(self) -> bool:
        """Check if sidebar is visible."""
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.SIDEBAR_CONTAINER)
            )
            return element.is_displayed()
        except Exception:
            return False

    def get_menu_items(self) -> list:
        """Get all menu items in the sidebar."""
        self.wait.until(EC.visibility_of_element_located(self.SIDEBAR_CONTAINER))
        items = self.driver.find_elements(*self.MENU_ITEMS)
        return [item.text for item in items]

    def click_menu_item(self, item_text: str) -> bool:
        """
        Click a menu item by its text.

        Args:
            item_text: Text of the menu item to click

        Returns:
            True if item was clicked, False otherwise
        """
        items = self.driver.find_elements(*self.MENU_ITEMS)
        for item in items:
            if item.text == item_text:
                item.click()
                return True
        return False

    def toggle_sidebar(self) -> None:
        """Toggle sidebar visibility."""
        toggle = self.wait.until(
            EC.element_to_be_clickable(self.TOGGLE_BUTTON)
        )
        toggle.click()

    def collapse_sidebar(self) -> None:
        """Collapse the sidebar."""
        collapse = self.wait.until(
            EC.element_to_be_clickable(self.COLLAPSE_BUTTON)
        )
        collapse.click()
