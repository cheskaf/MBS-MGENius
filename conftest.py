import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
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

def pytest_configure(config):
    config.addinivalue_line("markers", "admin: mark test as admin test")