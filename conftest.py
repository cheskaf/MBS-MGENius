import pytest
import os
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None, help="Specify a browser to run")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")

def pytest_configure(config):
    config.addinivalue_line("markers", "admin: mark test as admin test")
    allure.dynamic.parameter("executor", os.getenv("CI_AGENT", "Local Machine")) # Executor info
    allure.dynamic.parameter("build", os.getenv("BUILD_ID", "dev-001")) # Build info
    allure.dynamic.parameter("branch", os.getenv("GIT_BRANCH", "main")) # Branch info
    
# Default browsers if no --browser is specified
default_browsers = ["chrome"] # Edge still has some issues

@pytest.fixture(params=default_browsers)
def driver(request):
    # Check for command-line override
    cli_browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    # If CLI browser is specified, override param
    browser = cli_browser.lower() if cli_browser else request.param

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        from selenium.webdriver.firefox.options import Options as FirefoxOptions
        options = FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

    elif browser == "edge":
        options = EdgeOptions()
        options.use_chromium = True
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")    
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        options.add_argument(f"--user-data-dir=C:/Temp/EdgeProfile")
        options.add_argument("--disable-features=msEdgeIdentity,EnableEphemeralProfiles")
        driver = webdriver.Edge(options=options)
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

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Only take action on test failure in the call phase
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")  # access driver fixture
        if driver:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            screenshot_name = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_name)
            # Attach to Allure
            allure.attach.file(screenshot_name, name="Screenshot", attachment_type=allure.attachment_type.PNG)

def pytest_sessionfinish(session, exitstatus):
    env_path = os.path.join(os.getcwd(), "allure-results", "environment.properties")
    os.makedirs(os.path.dirname(env_path), exist_ok=True)
    with open(env_path, "w") as f:
        browser = session.config.getoption("--browser") or "Multiple Browsers"
        f.write(f"Browser={browser}\n")
        f.write(f"OS={os.name}\n")
        f.write(f"URL={os.getenv('BASE_URL', 'No base URL set in environment file')}\n")
        # check if headless
        headless = session.config.getoption("--headless")
        f.write(f"Headless={headless}\n")