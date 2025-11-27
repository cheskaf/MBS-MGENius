"""Test configuration module containing URLs and user credentials."""

import os


class Config:
    """Configuration class for test settings."""

    # Base URL for the application under test
    BASE_URL = os.environ.get("BASE_URL", "https://example.com")

    # Browser settings
    BROWSER = os.environ.get("BROWSER", "chrome")
    HEADLESS = os.environ.get("HEADLESS", "true").lower() == "true"

    # Timeouts (in seconds)
    IMPLICIT_WAIT = int(os.environ.get("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.environ.get("EXPLICIT_WAIT", "20"))
    PAGE_LOAD_TIMEOUT = int(os.environ.get("PAGE_LOAD_TIMEOUT", "30"))


class TestUsers:
    """Test user credentials."""

    # Standard test user
    STANDARD_USER = {
        "username": os.environ.get("TEST_USERNAME", "test_user"),
        "password": os.environ.get("TEST_PASSWORD", "test_password"),
    }

    # Admin test user
    ADMIN_USER = {
        "username": os.environ.get("ADMIN_USERNAME", "admin_user"),
        "password": os.environ.get("ADMIN_PASSWORD", "admin_password"),
    }
