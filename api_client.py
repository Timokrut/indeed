import requests 
from enum import StrEnum

class Role(StrEnum):
    user = "user"
    moderator = "moderator"
    admin = "admin"

class NoteType(StrEnum):
    public = "public"
    private = "private"
    role = "role"
 
class ApiClient:
    URL = 'https://secby.ru'
    
    def __init__(self) -> None:
        # Auth data
        self._access_token = None

    # AUTHENTICATION
    def login(self, username: str, password: str) -> requests.Response:
        payload = {
            "username": username,
            "password": password
        }

        try: 
            response = requests.post(f"{self.URL}/api/auth/login", json=payload)
            if response.status_code == 200:
                self._access_token = response.json()["access_token"]
            
            return response
        
        except requests.RequestException as e:
            raise RuntimeError(f"Something went wrong while logging in: {e}")
    
    def get_access_token(self) -> str:
        if self._access_token is None:
            raise RuntimeError("User not authenticated. Login first")
        return self._access_token

    def set_access_token(self, token: str) -> None:
        self._access_token = token   
    
    def get_headers(self) -> dict[str, str]:
        token = self.get_access_token()

        return {
            "Authorization": f"Bearer {token}"
        }

    def verify_token(self) -> requests.Response:
        response = requests.post(f"{self.URL}/api/auth/verify", headers=self.get_headers())
        return response

    def change_password(self, old_password: str, new_password: str) -> requests.Response:
        payload = {
            "old_password": old_password,
            "new_password": new_password
        }

        response = requests.post(f"{self.URL}/api/auth/change-password", json=payload, headers=self.get_headers())
        return response

    def set_password(self, account_id: int, new_password: str) -> requests.Response:
        payload = {
            "account_id": account_id,
            "new_password": new_password
        }
        
        response = requests.post(f"{self.URL}/api/auth/set-password", json=payload, headers=self.get_headers())
        return response

    # PROFILES
    def create_profile(
        self, 
        name: str | None = None, 
        surname: str | None = None, 
        middlename: str | None = None, 
        birthdate: str | None = None, # "YYYY-MM-DD"
        about: str | None = None, 
        links: str | None = None) -> requests.Response:

        payload = {
            "name": name, 
            "surname": surname, 
            "middlename": middlename, 
            "birthdate": birthdate,
            "about": about, 
            "links": links
        }

        response = requests.post(f"{self.URL}/api/profiles/", json=payload, headers=self.get_headers())
        return response

    def get_profiles(self, limit: int = 100, offset: int = 0) -> requests.Response:
        payload = {
            "limit": limit, 
            "offset": offset
        }

        response = requests.get(f"{self.URL}/api/profiles/", params=payload, headers=self.get_headers())
        return response

    def get_current_profile(self) -> requests.Response:
        response = requests.get(f"{self.URL}/api/profiles/me", headers=self.get_headers())
        return response
        
    def update_current_profile(
        self, 
        name: str | None = None, 
        surname: str | None = None, 
        middlename: str | None = None, 
        birthdate: str | None = None, # "YYYY-MM-DD"
        about: str | None = None, 
        links: str | None = None) -> requests.Response:
        
        payload = {
            "name": name, 
            "surname": surname, 
            "middlename": middlename, 
            "birthdate": birthdate,
            "about": about, 
            "links": links
        }

        response = requests.put(f"{self.URL}/api/profiles/me", json=payload, headers=self.get_headers())
        return response

    def get_profile_by_id(self, account_id: int) -> requests.Response:
        response = requests.get(f"{self.URL}/api/profiles/{account_id}", headers=self.get_headers())
        return response

    def update_profile_by_id(
        self, 
        account_id: int,
        name: str | None = None, 
        surname: str | None = None, 
        middlename: str | None = None, 
        birthdate: str | None = None, # "YYYY-MM-DD"
        about: str | None = None, 
        links: str | None = None) -> requests.Response:

        payload = {
            "name": name, 
            "surname": surname, 
            "middlename": middlename, 
            "birthdate": birthdate,
            "about": about, 
            "links": links
        }
        
        response = requests.put(f"{self.URL}/api/profiles/{account_id}", json=payload, headers=self.get_headers())
        return response
        
    def delete_account(self, account_id: int) -> requests.Response:
        response = requests.delete(f"{self.URL}/api/profiles/{account_id}", headers=self.get_headers())
        return response

    def update_account_role(self, account_id: int, role: Role) -> requests.Response:
        payload = {
            "role_name": role
        }

        response = requests.put(f"{self.URL}/api/profiles/{account_id}/role", params=payload, headers=self.get_headers())
        return response
    
    # RESOURCE NOTES
    def get_notes(self, limit: int = 100, offset: int = 0) -> requests.Response:
        if not(1 <= limit <= 1000): 
            raise RuntimeError("Limit must be MIN 1, MAX 1000")
        
        if offset < 0:
            raise RuntimeError("Offset must be greater than 0")
    
        payload = {
            "limit": limit, 
            "offset": offset
        }

        response = requests.get(f"{self.URL}/api/notes/", params=payload, headers=self.get_headers())
        return response

    def create_note(self, name: str, notes: str, note_type: NoteType, role_id: int = 0) -> requests.Response:
        payload = {
            "name": name, 
            "notes": notes,
            "type": note_type, 
            "role_id": role_id
        }

        response = requests.post(f"{self.URL}/api/notes/", json=payload, headers=self.get_headers())
        return response

    def get_note_by_id(self, resource_id: int) -> requests.Response:
        response = requests.get(f"{self.URL}/api/notes/{resource_id}", headers=self.get_headers())
        return response
    
    def update_note_by_id(self, resource_id: int, name: str, notes: str, note_type: NoteType, role_id: int = 0) -> requests.Response:
        payload = {
            "name": name, 
            "notes": notes,
            "type": note_type, 
            "role_id": role_id
        }

        response = requests.put(f"{self.URL}/api/notes/{resource_id}", json=payload, headers=self.get_headers())
        return response
    
    def delete_note_by_id(self, resource_id: int) -> requests.Response:
        response = requests.delete(f"{self.URL}/api/notes/{resource_id}", headers=self.get_headers())
        return response