ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

KEY = 3

def caesar_encrypt(plain_text):
  for x in plain_text:
    index = ALPHABET.find(x)
