import requests
from datetime import datetime


class WritingToTheServer:

    def __init__(self, server_url):
        self.server_url = server_url

    def get_current_time(self):
        return datetime.now()

    def send_log(self, message):
        data = {"message": message}#now need to send that with time
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.server_url, json=data, headers=headers)
        print(response.json())
