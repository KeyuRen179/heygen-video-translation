import requests
import time

class TranslationClient:
    def __init__(self, server_url, max_retries=10, initial_interval=1, max_interval=5):
        self.server_url = server_url
        self.max_retries = max_retries
        self.initial_interval = initial_interval
        self.max_interval = max_interval

    def get_status(self):
        retries = 0
        interval = self.initial_interval

        while retries < self.max_retries:
            response = requests.get(f"{self.server_url}/status")
            status = response.json().get("result")

            if status in ["completed", "error"]:
                return status

            time.sleep(interval)
            interval = min(interval * 2, self.max_interval)
            retries += 1

        return "timeout"

if __name__ == "__main__":
    client = TranslationClient("http://localhost:5000")
    print("Translation Status:", client.get_status())
