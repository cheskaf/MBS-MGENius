# MBS-MGENius

Selenium + pytest test automation framework with HTML and Allure reporting.

## Project Structure

```
project/
│
├── tests/                  # Test scripts (pytest)
│   └── test_example.py
├── Elements/               # Page object classes
│   └── sidebar.py
├── utils/                  # Helper scripts (login)
│   └── login.py
├── config/                 # Test configuration (users, urls)
│   └── config.py
├── conftest.py             # Pytest fixtures
├── requirements.txt        # Python dependencies
└── README.md               # Setup instructions
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Chrome or Firefox browser

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cheskaf/MBS-MGENius.git
   cd MBS-MGENius
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Set environment variables to configure the tests:

```bash
# Base URL for testing
export BASE_URL="https://your-app-url.com"

# Browser selection (chrome/firefox)
export BROWSER="chrome"

# Headless mode (true/false)
export HEADLESS="true"

# Test user credentials
export TEST_USERNAME="your_username"
export TEST_PASSWORD="your_password"
```

## Running Tests

### Basic Test Run

```bash
pytest tests/
```

### Run with pytest-html Report

```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

### Run with Allure Report

1. Run tests with Allure:
   ```bash
   pytest tests/ --alluredir=allure-results
   ```

2. Generate and view the report:
   ```bash
   allure serve allure-results
   ```

### Additional Options

```bash
# Run tests in headed mode (visible browser)
pytest tests/ --no-headless

# Run with specific browser
pytest tests/ --browser=firefox

# Run only smoke tests
pytest tests/ -m smoke

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_example.py

# Run specific test class
pytest tests/test_example.py::TestExample

# Run specific test method
pytest tests/test_example.py::TestExample::test_page_title
```

## Writing Tests

### Example Test

```python
import allure
import pytest

@allure.feature("My Feature")
class TestMyFeature:
    
    @allure.title("Test description")
    def test_example(self, driver, base_url):
        driver.get(base_url)
        assert driver.title == "Expected Title"
```

### Using Page Objects

```python
from Elements.sidebar import Sidebar

def test_sidebar(self, driver, base_url):
    driver.get(base_url)
    sidebar = Sidebar(driver)
    assert sidebar.is_visible()
```

### Using Login Helper

```python
from utils.login import LoginHelper
from config.config import TestUsers

def test_login(self, driver, base_url):
    driver.get(base_url)
    login = LoginHelper(driver)
    user = TestUsers.STANDARD_USER
    success = login.login(user["username"], user["password"])
    assert success
```

## Reports

### pytest-html

Generates a standalone HTML report with test results, screenshots, and logs.

```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

### Allure

Generates an interactive HTML report with detailed test information.

```bash
# Generate results
pytest tests/ --alluredir=allure-results

# Serve report locally
allure serve allure-results

# Generate static report
allure generate allure-results -o allure-report
```

## License

MIT License