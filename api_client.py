import requests 

class ApiClient:
    URL = 'https://secby.ru'
    
    def __init__(self) -> None:
        self._access_token = None

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
            raise Exception("User not authenticated. Login first")
        return self._access_token

    def set_access_token(self, token: str) -> None:
        self._access_token = token   
    
    def get_headers(self):
        token = self.get_access_token()

        return {
            "Authorization": f"Bearer {token}"
        }

    def verify_token(self) -> bool:
        response = requests.post(f"{self.URL}/api/auth/verify", headers=self.get_headers())
        return response.status_code == 200

    def change_password(self, old_password: str, new_password: str) -> requests.Response:
        payload = {
            "old_password": old_password,
            "new_password": new_password
        }

        response = requests.post(f"{self.URL}/api/auth/change-password", json=payload, headers=self.get_headers())
        return response