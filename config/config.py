"""Test configuration module containing URLs and user credentials."""

import json
import os
from pathlib import Path

# Get the config directory path
CONFIG_DIR = Path(__file__).parent


def _load_json(filename: str) -> dict:
    """Load JSON file from config directory."""
    filepath = CONFIG_DIR / filename
    if filepath.exists():
        try:
            with open(filepath, "r") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Warning: Failed to parse {filename}: {e}")
    return {}


# Load JSON configuration files
_urls = _load_json("urls.json")
_users = _load_json("users.json")


class Config:
    """Configuration class for test settings."""

    # Base URL for the application under test (env var overrides JSON)
    BASE_URL = os.environ.get("BASE_URL", _urls.get("base_url", "https://example.com"))
    LOGIN_URL = os.environ.get("LOGIN_URL", _urls.get("login_url", "/login"))
    DASHBOARD_URL = os.environ.get("DASHBOARD_URL", _urls.get("dashboard_url", "/dashboard"))
    API_URL = os.environ.get("API_URL", _urls.get("api_url", "https://api.example.com"))

    # Browser settings
    BROWSER = os.environ.get("BROWSER", "chrome")
    HEADLESS = os.environ.get("HEADLESS", "true").lower() == "true"

    # Timeouts (in seconds)
    IMPLICIT_WAIT = int(os.environ.get("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.environ.get("EXPLICIT_WAIT", "20"))
    PAGE_LOAD_TIMEOUT = int(os.environ.get("PAGE_LOAD_TIMEOUT", "30"))


class TestUsers:
    """Test user credentials."""

    # Standard test user (env var overrides JSON)
    _standard = _users.get("standard_user", {})
    STANDARD_USER = {
        "username": os.environ.get("TEST_USERNAME", _standard.get("username", "test_user")),
        "password": os.environ.get("TEST_PASSWORD", _standard.get("password", "test_password")),
    }

    # Admin test user (env var overrides JSON)
    _admin = _users.get("admin_user", {})
    ADMIN_USER = {
        "username": os.environ.get("ADMIN_USERNAME", _admin.get("username", "admin_user")),
        "password": os.environ.get("ADMIN_PASSWORD", _admin.get("password", "admin_password")),
    }
