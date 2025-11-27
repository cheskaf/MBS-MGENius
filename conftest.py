"""Pytest fixtures for Selenium tests."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config.config import Config


def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line("markers", "smoke: mark test as smoke test")


def pytest_addoption(parser):
    """Add custom command line options."""
    parser.addoption(
        "--browser",
        action="store",
        default=Config.BROWSER,
        help="Browser to use for tests (chrome/firefox)",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=Config.HEADLESS,
        help="Run browser in headless mode",
    )


@pytest.fixture(scope="session")
def browser_name(request):
    """Get browser name from command line or config."""
    return request.config.getoption("--browser").lower()


@pytest.fixture(scope="session")
def headless(request):
    """Get headless mode from command line or config."""
    return request.config.getoption("--headless")


@pytest.fixture(scope="function")
def driver(browser_name, headless):
    """
    Create and configure WebDriver instance.

    Yields:
        WebDriver instance configured for the specified browser
    """
    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def base_url():
    """Get base URL for tests."""
    return Config.BASE_URL
