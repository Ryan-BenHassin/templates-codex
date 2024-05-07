#TODO
import jwt
import datetime

class Authentication:
 def __init__(self, secret_key, algorithm):
 self.secret_key = secret_key
 self.algorithm = algorithm

 def generate_token(self, username, password, expires_in=3600):
 payload = {
 'username': username,
 'password': password,
 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)
 }
 token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
 return token

 def verify_token(self, token):
 try:
 payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
 return payload
 except jwt.ExpiredSignatureError:
 return 'Signature expired'
 except jwt.InvalidTokenError:
 return 'Invalid token'

auth = Authentication('secret_key_here', 'HS256')
print(auth.generate_token('user', 'password'))
print(auth.verify_token('token_here'))
