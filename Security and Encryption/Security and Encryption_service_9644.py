#TODO
from cryptography.fernet import Fernet

def generate_key():
 key = Fernet.generate_key()
 return key

def encrypt_message(message, key):
 cipher_suite = Fernet(key)
 cipher_text = cipher_suite.encrypt(message.encode())
 return cipher_text

def decrypt_message(cipher_text, key):
 cipher_suite = Fernet(key)
 plain_text = cipher_suite.decrypt(cipher_text)
 return plain_text.decode()

def main():
 key = generate_key()
 print("Generated Key: ", key.decode())

 message = input("Enter message to encrypt: ")
 cipher_text = encrypt_message(message, key)
 print("Encrypted Message: ", cipher_text)

 plain_text = decrypt_message(cipher_text, key)
 print("Decrypted Message: ", plain_text)

if __name__ == "__main__":
 main()
