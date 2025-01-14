ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

KEY = 3

def caesar_encrypt(plain_text):
  cipher_text = ''
  plain_text.upper()

  for x in plain_text:
    index = ALPHABET.find(x)
    index = (index + KEY) % len(ALPHABET)
    cipher_text = cipher_text + ALPHABET[index]
  return cipher_text
