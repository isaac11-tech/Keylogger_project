import random
class Encryption:
    def __init__(self, chars):
        self.chars = chars
        self.TXT = 'The quick brown fox jumps over 13 lazy dogs & finds 24 hidden keys'
        self.randint = random.randint(0, len(self.TXT)-1)
        self.key = self.TXT[self.randint]

    def encryption_text(self):
        arr = [(ord(i) ^ ord(self.key)) for i in self.chars]
        cipher = [chr(i) for i in arr]
        return [self.randint, cipher]


class Decoding:
    def __init__(self, cipher):
        self.cipher = cipher[1]
        self.TXT = 'The quick brown fox jumps over 13 lazy dogs & finds 24 hidden keys'
        self.key = cipher[0]
        self.decoding = ""

    def decoding_cipher(self):
        arr = [(ord(i) ^ ord(self.TXT[self.key])) for i in self.cipher]
        for i in arr:
            self.decoding += chr(i)
        return self.decoding

a = Encryption('אח שלי אתה')
print(a.encryption_text())
b = Decoding(a.encryption_text())
print(b.decoding_cipher())
