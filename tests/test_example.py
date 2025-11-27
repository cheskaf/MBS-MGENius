"""Example test module demonstrating Selenium + pytest usage."""

import allure
import pytest
from selenium.webdriver.common.by import By


@allure.feature("Example Tests")
@allure.story("Page Loading")
class TestExample:
    """Example test class demonstrating basic Selenium tests."""

    @allure.title("Test page title")
    @allure.description("Verify that the page title is correct after navigation")
    def test_page_title(self, driver, base_url):
        """Test that page loads with correct title."""
        driver.get(base_url)
        assert driver.title is not None
        allure.attach(
            driver.get_screenshot_as_png(),
            name="page_screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

    @allure.title("Test page loads successfully")
    @allure.description("Verify that the page loads without errors")
    def test_page_loads(self, driver, base_url):
        """Test that page loads successfully."""
        driver.get(base_url)
        # Check that body element exists (page loaded)
        body = driver.find_element(By.TAG_NAME, "body")
        assert body is not None

    @allure.title("Test URL is correct")
    @allure.description("Verify that the current URL matches the expected URL")
    def test_url_correct(self, driver, base_url):
        """Test that URL is correct after navigation."""
        driver.get(base_url)
        assert base_url in driver.current_url


@allure.feature("Example Tests")
@allure.story("Browser Functionality")
class TestBrowserFunctions:
    """Test class for browser functionality tests."""

    @allure.title("Test browser navigation")
    @allure.description("Verify browser back/forward navigation works")
    def test_browser_navigation(self, driver, base_url):
        """Test browser back/forward navigation."""
        driver.get(base_url)
        initial_url = driver.current_url

        # Navigate to another page (using a common path)
        driver.get(f"{base_url}/about")

        # Go back
        driver.back()
        assert driver.current_url == initial_url or base_url in driver.current_url

    @allure.title("Test page refresh")
    @allure.description("Verify that page refresh works correctly")
    def test_page_refresh(self, driver, base_url):
        """Test that page refresh works."""
        driver.get(base_url)
        driver.refresh()
        body = driver.find_element(By.TAG_NAME, "body")
        assert body is not None


@pytest.mark.smoke
@allure.feature("Smoke Tests")
class TestSmoke:
    """Smoke tests for quick verification."""

    @allure.title("Smoke test - page accessible")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_smoke_page_accessible(self, driver, base_url):
        """Smoke test to verify page is accessible."""
        driver.get(base_url)
        assert driver.current_url is not None
