from httpx import Client, HTTPStatusError
from typing import Optional, Any, Dict
from .utils import header, objects


class Tiu:
    """
    Main class for interacting with the TIU student portal.
    
    Attributes:
        base_url (str): Base URL for the TIU portal
        proxies (Optional[dict]): Proxy configuration for requests
        sid (Optional[str]): Session ID for authentication
        request_timeout (int): Timeout for HTTP requests in seconds
        profile (objects.UserProfile): User profile information
    """

    def __init__(self, proxies: Optional[dict] = None, request_timeout: Optional[int] = 60):
        """
        Initialize the TIU client.

        Args:
            proxies: Optional proxy configuration
            request_timeout: Request timeout in seconds
        """
        self.base_url = "https://my.tiu.edu.iq"
        self.proxies = proxies
        self.sid = None
        self.request_timeout = request_timeout
        self.profile = objects.UserProfile()

    def make_request(
        self, 
        method: str, 
        endpoint: str, 
        data: Optional[Dict[str, Any]] = None, 
        params: Optional[Dict[str, Any]] = None
    ):
        """
        Make an HTTP request to the TIU portal.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            data: Request data (for POST requests)
            params: Query parameters

        Returns:
            Response object from the request

        Raises:
            Exception: If the request fails
        """
        url = f"{self.base_url}{endpoint}"
        request_headers = header.Headers(self.sid).get_headers()

        with Client(proxies=self.proxies, timeout=self.request_timeout) as client:
            try:
                response = client.request(
                    method, 
                    url, 
                    headers=request_headers, 
                    data=data, 
                    params=params
                )
                response.raise_for_status()
                return response
            except HTTPStatusError as e:
                raise Exception(f"Request failed: {e}")

    def _get_profile_info(self) -> str:
        """
        Fetch the user's profile information.

        Returns:
            HTML content of the profile page
        """
        response = self.make_request("GET", endpoint="/pages/home.php")
        return response.text

    def login(self, username: str, password: str) -> str:
        """
        Login using username and password.

        Args:
            username: TIU username
            password: TIU password

        Returns:
            Success message
        """
        data = {
            'username': username,
            'password': password,
            'login.x': '0',
            'login.y': '0'
        }

        response = self.make_request("POST", endpoint="/", data=data)
        self.sid = response.cookies.get("PHPSESSID")
        self.profile = objects.UserProfile()
        self.profile.from_html(self._get_profile_info())
        return "Login successful."

    def sid_login(self, sid: str) -> str:
        """
        Login using an existing session ID.

        Args:
            sid: Session ID from a previous login

        Returns:
            Success message
        """
        self.sid = sid
        self.profile = objects.UserProfile()
        self.profile.from_html(self._get_profile_info())
        return "SID Login successful."

    def logout(self) -> str:
        """
        Logout and clear the session.

        Returns:
            Success message
        """
        self.make_request("GET", endpoint="/pages/p999.php/")
        self.sid = None
        return "Logout successful."

    def get_courses_data(self) -> objects.CourseData:
        """
        Fetch and return course data.

        Returns:
            CourseData object containing course information
        """
        response = self.make_request("GET", endpoint="/pages/p103.php")
        course_data = objects.CourseData()
        course_data.from_html(response.text)
        return course_data

    def get_personal_info(self) -> objects.PersonalInfo:
        """
        Fetch and return detailed personal information.

        Returns:
            PersonalInfo object containing detailed user information
        """
        response = self.make_request("GET", endpoint="/pages/p201.php")
        personal_info = objects.PersonalInfo()
        personal_info.from_html(response.text)
        return personal_info
