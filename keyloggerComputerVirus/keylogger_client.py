import requests

class WritingToTheServer:

    def __init__(self, server_url):
        self.server_url = server_url

    def send_log(self, message):
        data = {"message": message}
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.server_url, json=data,headers=headers)
        print(response.json())


logger = WritingToTheServer("http://127.0.0.1:5000")
logger.send_log("User pressed: A")
logger.send_log("User pressed: B")