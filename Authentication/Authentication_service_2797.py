import Flask
from flask import request, jsonify
from flask_restful import Resource, Api
from functools import wraps
import jwt

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'super-secret'

def authenticate(f):
 @wraps(f)
 def decorated_function(*args, **kwargs):
 auth_header = request.headers.get('Authorization')
 if auth_header:
 try:
 token = auth_header.split(" ")[1]
 data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
 return f(*args, **kwargs)
 except jwt.ExpiredSignatureError:
 return jsonify({'error': 'Token has expired'}), 401
 except jwt.InvalidTokenError:
 return jsonify({'error': 'Invalid token'}), 401
 else:
 return jsonify({'error': 'Unauthorized access'}), 401
 return decorated_function

class Auth(Resource):
 def post(self):
 auth = request.authorization
 if auth and auth.username == 'username' and auth.password == 'password':
 token = jwt.encode({'username': auth.username}, app.config['SECRET_KEY'], algorithm='HS256')
 return jsonify({'token': token.decode('UTF-8')})
 return jsonify({'error': 'Unauthorized access'}), 401

api.add_resource(Auth, '/auth')

if __name__ == "__main__":
 app.run(debug=True)
