import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser: chrome or firefox"
    )
    parser.addoption(
        "--headless", action="store_true", help="Run tests in headless mode"
    )

def pytest_configure(config):
    config.addinivalue_line("markers", "admin: mark test as admin test")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser.lower() == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser.lower() == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    url = os.getenv("BASE_URL")
    assert url, "BASE_URL environment variable is missing."
    return url

@pytest.fixture(scope="session")
def superadmin_credentials():
    return {
        "email": os.getenv("SUPERADMIN_EMAIL"),
        "password": os.getenv("SUPERADMIN_PASSWORD")
    }