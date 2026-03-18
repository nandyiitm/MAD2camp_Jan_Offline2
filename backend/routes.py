from flask_restful import Resource, Api
from flask import request


api = Api()

# @app.route('/hello')
# def hello_world():
#     if request.method == 'GET':
#        return 'Hello, World!'
#     elif request.method == 'POST':
#        return 'Hello, World!', 201

class HelloWorldResource(Resource):
    def get(self):
        message = "Hello, World!"
        return {'message': message, 'method': 'GET'}, 200
    def post(self):
        data = request.get_json()
        print('received data:',data)
        message = f"Hello, {data.get('name', 'World')}!"
        return {'message': message, 'method': 'POST'}, 201
    def put(self):
        message = "Hello, World!"
        return {'message': message, 'method': 'PUT'}, 200
    def delete(self):
        return {'message': 'Hello, World! DELETED', 'method': 'DELETE'}, 204
api.add_resource(HelloWorldResource, '/hello')