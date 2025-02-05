class Headers:
    def __init__(self, sid: Optional[str] = None):
        self.sid = sid

    def get_headers(self) -> dict:
        """Generate headers with optional session ID"""
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://my.tiu.edu.iq/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

        if self.sid:
            headers["Cookie"] = f"PHPSESSID={self.sid}"
        return headers
