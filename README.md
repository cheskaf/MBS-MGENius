# MBS-MGENius

This repository contains automated tests using Selenium WebDriver, Pytest, and Allure Reports. Tests follow the Page Object Model (POM).

## Project Structure

```
project/
│
├── tests/                  # Test scripts organized by role
│   └── test_admin/         # Admin-related tests
│       └── test_A1_login.py
│
├── pages/                  # Page Object Model classes
│   └── admin_pages/
│   │   ├── login_page.py
│   │   └── dashboard_page.py
│   └── base_page.py        # BasePage with reusable methods
│
├── config/                 # Configuration files
│   └── urls.py             # Page URLs
│
├── conftest.py             # Pytest fixtures (driver)
├── requirements.txt        # Python dependencies
└── README.md
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Chrome or Firefox browser
- Git

### Installation

1. Clone the repository
   
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Setup environment variables
   
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

### Basic Test Run

```bash
pytest tests/
```


### Additional Options

```bash
# Run tests in headed mode (visible browser)
pytest tests/ --no-headless

# Run tests in headless mode
pytest tests/ --alluredir=allure-results --browser chrome --headless

# Run with specific browser
pytest tests/ --browser=firefox

# Run only admin tests
pytest tests/ -m admin

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_example.py
pytest tests/test_admin/test_A1_login.py

# Run specific test class
pytest tests/test_example.py::TestExample

# Run specific test method
pytest tests/test_example.py::TestExample::test_page_title
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

## Notes

### Pages (`pages/`)

* **BasePage**: Common methods like `click`, `send_keys`, `get_text`, `navigate_to`, and waits.
* For **Allure**, prefer `@allure.step` inside Page Object methods for better traceability.

### Tests (`tests/`)

* **Class-based grouping** for shared Allure labels (`epic` and `feature`).

### Future enhancements
- Dockerized Selenium for CI/CD
- Headless browser execution
- Reporting screenshots on failure

