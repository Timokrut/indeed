import os
from api_client import Role


def test_admin_can_get_user_profile(admin_client):
    response = admin_client.get_profile_by_id(os.getenv("TEST_USER_ID"))

    assert response.status_code == 200

def test_admin_can_change_role(admin_client):
    response = admin_client.update_account_role(
        account_id=os.getenv("TEST_USER_ID"),
        role=Role.user
    )

    assert response.status_code == 200

def test_admin_can_update_profile(admin_client):
    response = admin_client.update_profile_by_id(
        account_id=os.getenv("TEST_USER_ID"),
        about="Updated by admin"
    )

    assert response.status_code == 200

def test_admin_cannot_set_password(admin_client):
    # only SUPERADMIN can
    response = admin_client.set_password(
        account_id=os.getenv("TEST_USER_ID"),
        new_password="temporary_password"
    )

    assert response.status_code == 403