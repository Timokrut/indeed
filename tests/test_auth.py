import os
import pytest


def test_login_success(api_client):
    response = api_client.login(
        os.getenv("USER_USERNAME"),
        os.getenv("USER_PASSWORD")
    )
    assert response.status_code == 200

    data = response.json()
    assert "access_token" in data

def test_login_invalid_password(api_client):
    response = api_client.login(
        os.getenv("USER_USERNAME"),
        "wrong_password"
    )

    assert response.status_code == 401

def test_login_invalid_user(api_client):
    response = api_client.login(
        "unknown_user",
        os.getenv("USER_PASSWORD")
    )

    assert response.status_code == 401

def test_login_empty_credentials(api_client):
    response = api_client.login("", "")

    assert response.status_code == 401

def test_verify_valid_token(authorized_client):
    response = authorized_client.verify_token()
    
    assert response.status_code == 200


def test_verify_invalid_token(api_client):
    api_client.set_access_token("fake_token")
    response = api_client.verify_token()
    
    assert response.status_code == 401

def test_verify_without_token(api_client):
    response = api_client.verify_token()

    assert response.status_code == 401

def test_change_password_success(authorized_client):
    old_password = os.getenv("USER_PASSWORD")
    new_password = "new_password123"

    response = authorized_client.change_password(
        old_password,
        new_password
    )

    assert response.status_code == 200

    authorized_client.change_password(
        new_password,
        old_password
    )

def test_change_password_invalid_old_password(authorized_client):
    response = authorized_client.change_password(
        "wrong_old_password",
        "new_password"
    )

    assert response.status_code == 400

def test_change_password_unauthorized(api_client):
    api_client.set_access_token("fake_token")
    response = api_client.change_password(
        os.getenv("USER_PASSWORD"),
        "new_password"
    )

    assert response.status_code == 401

def test_user_cannot_set_password(authorized_client):
    response = authorized_client.set_password(
        account_id=os.getenv("ADMIN_ID"),
        new_password="new_password"
    )

    assert response.status_code == 403