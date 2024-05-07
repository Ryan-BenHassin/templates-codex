# TODO
from cryptography.fernet import Fernet
import os
import base64

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

generate_key()
message = "Hello, World!"
encrypted_message = encrypt_message(message)
print("Encrypted message: ", encrypted_message)
decrypted_message = decrypt_message(encrypted_message)
print("Decrypted message: ", decrypted_message)