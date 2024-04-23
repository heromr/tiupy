from httpx import Client
from typing import Optional, Any, Dict
from .utils import headers, objects


class Tiu:
    def __init__(self, proxies: Optional[dict] = None, request_timeout: Optional[int] = 60):
        self.base_url = "https://my.tiu.edu.iq"
        self.proxies = proxies

        self.sid = None
        self.request_timeout = request_timeout
        self.profile = objects.UserProfile(None)

    def make_request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None):
        url = self.base_url + endpoint
        with Client(proxies=self.proxies, timeout=self.request_timeout) as client:
            response = client.request(method, url, headers=headers.Headers().headers, data=data, params=params)
            response.raise_for_status()
            return response
    
    def _get_profile_info(self):
        response = self.make_request("GET", endpoint="/pages/home.php")
        return response.text
    
    def login(self, username: str, password: str):
        data = {
            'username': username,
            'password': password,
            'login.x': '0',  # Need to change?
            'login.y': '0'   # Need to change?
        }

        response = self.make_request("POST", endpoint="/", data=data)

        self.sid = response.cookies.get("PHPSESSID")
        headers.sid = self.sid
        self.profile = objects.UserProfile(self._get_profile_info())
        return response.status_code
    
    def sid_login(self, SID: str):
        self.sid = SID
        headers.sid = self.sid
        self.profile = objects.UserProfile(self._get_profile_info())
        return
    
    def logout(self):
        response = self.make_request("GET", endpoint="/pages/p999.php/")
        return response.status_code
    
    def get_courses_data(self):
        response = self.make_request("GET", endpoint="/pages/p103.php")
        return objects.CourseData(response.text)
