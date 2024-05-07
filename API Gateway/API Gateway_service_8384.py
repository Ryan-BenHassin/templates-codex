#TODO
from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
   def get(self):
       return {"message": "Welcome to API Gateway"}

class Users(Resource):
   def get(self):
       return [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Doe"}]

class User(Resource):
   def get(self, id):
       return {"id": id, "name": f"User {id}"}

api.add_resource(HelloWorld, '/')
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:id>')

if __name__ == '__main__':
   app.run(debug=True)