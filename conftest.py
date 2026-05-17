import os
import pytest

from api_client import ApiClient
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

USER_USERNAME = os.getenv("USER_USERNAME", "")
USER_PASSWORD = os.getenv("USER_PASSWORD", "")

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")

MODERATOR_USERNAME = os.getenv("MODERATOR_USERNAME", "")
MODERATOR_PASSWORD = os.getenv("MODERATOR_PASSWORD", "")

@pytest.fixture
def api_client():
    return ApiClient()

@pytest.fixture
def authorized_client():
    client = ApiClient()

    response = client.login(
        USER_USERNAME,
        USER_PASSWORD
    )
    assert response.status_code == 200
    
    return client

@pytest.fixture
def admin_client():
    client = ApiClient()

    response = client.login(
        ADMIN_USERNAME,
        ADMIN_PASSWORD
    )
    assert response.status_code == 200

    return client

@pytest.fixture
def moderator_client():
    client = ApiClient()

    response = client.login(
        MODERATOR_USERNAME,
        MODERATOR_PASSWORD
    )
    assert response.status_code == 200

    return client