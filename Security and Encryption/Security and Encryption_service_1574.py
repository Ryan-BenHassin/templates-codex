#TODO
import hashlib
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class SecurityAndEncryption:
 def __init__(self, password, salt):
 self.password = password
 self.salt = salt

 def hash_password(self):
 hashed_password = hashlib.sha256((self.password + self.salt).encode()).hexdigest()
 return hashed_password

 def generate_key(self):
 kdf = PBKDF2HMAC(
 algorithm=hashes.SHA256(),
 length=32,
 salt=self.salt.encode(),
 iterations=100000,
 backend=default_backend()
 )
 key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))
 return key

 def encrypt_data(self, data, key):
 f = Fernet(key)
 encrypted_data = f.encrypt(data.encode())
 return encrypted_data

 def decrypt_data(self, encrypted_data, key):
 f = Fernet(key)
 decrypted_data = f.decrypt(encrypted_data).decode()
 return decrypted_data

password = "your_password"
salt = "your_salt"
data = "your_data"

security = SecurityAndEncryption(password, salt)
hashed_password = security.hash_password()
key = security.generate_key()
encrypted_data = security.encrypt_data(data, key)
decrypted_data = security.decrypt_data(encrypted_data, key)

print("Hashed Password:", hashed_password)
print("Encrypted Data:", encrypted_data)
print("Decrypted Data:", decrypted_data)
