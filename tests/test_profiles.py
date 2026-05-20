import os
from api_client import Role


def test_get_current_profile(authorized_client):
    response = authorized_client.get_current_profile()
    assert response.status_code == 200

    data = response.json()
    assert "profile" in data["profile"].keys() # user dont have profile

def test_get_current_profile_unauthorized(api_client):
    api_client.set_access_token("fake")
    response = api_client.get_current_profile()

    assert response.status_code == 401
    
def test_get_profiles(authorized_client):
    response = authorized_client.get_profiles()

    assert response.status_code == 200
    assert isinstance(response.json()["profiles"], list)

def test_get_my_profile_by_id(authorized_client):
    response = authorized_client.get_profile_by_id(os.getenv("USER_ID"))

    assert response.status_code == 200

def test_get_somebodys_profile_by_id(authorized_client):
    response = authorized_client.get_profile_by_id(os.getenv("ADMIN_ID"))

    assert response.status_code == 403

def test_update_current_profile(authorized_client):
    response = authorized_client.update_current_profile(
        about="test message"
    )

    assert response.status_code == 200

def test_update_current_profile_unauthorized(api_client):
    api_client.set_access_token("fake")
    response = api_client.update_current_profile(
        about="test message"
    )

    assert response.status_code == 401

def test_user_cannot_update_other_profile(authorized_client):
    response = authorized_client.update_profile_by_id(
        account_id=os.getenv("ADMIN_ID"),
        about="test message"
    )

    assert response.status_code == 403

def test_user_cannot_delete_account(authorized_client):
    response = authorized_client.delete_account(os.getenv("ADMIN_ID"))

    assert response.status_code == 403

def test_user_cannot_change_role(authorized_client):
    response = authorized_client.update_account_role(
        account_id=os.getenv("ADMIN_ID"),
        role=Role.moderator
    )

    assert response.status_code == 403