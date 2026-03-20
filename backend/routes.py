from flask_restful import Resource, Api
from flask import request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_caching import Cache

from models import db, User, Mobile

api = Api()
cache = Cache()

# @app.route('/hello')
# def hello_world():
#     if request.method == 'GET':
#        return 'Hello, World!'
#     elif request.method == 'POST':
#        return 'Hello, World!', 201

#### Auth routes ####

class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        if not data.get('name') or not data.get('email') or not data.get('password'):
            return {'message': "All fields must be non-empty"}, 400
        is_user_exists = User.query.filter_by(email=data['email']).first()
        if is_user_exists:
            return {'message': "User with this email already exists"}, 409
        user = User(name=data['name'], email=data['email'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': f"User registered successfully!"}, 201
api.add_resource(RegisterResource, '/register')
    
class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        if not data.get('email') or not data.get('password'):
            return {'message': "Email and password are required"}, 400
        user = User.query.filter_by(email=data['email'], password=data['password']).first()
        if not user:
            return {'message': "Invalid email or password"}, 401
        access_token = create_access_token(identity=user.email)
        user = {'id': user.id, 'name': user.name, 'email': user.email, 'role': user.role}
        return {'message': f"User logged in successfully!", 'access_token': access_token, 'user': user}, 200
api.add_resource(LoginResource, '/login')

#### user and admin routes #####

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

import time

class MobileResource(Resource):

    # @jwt_required()
    @cache.cached(timeout=10)  # Cache GET responses for 60 seconds, vary by query string
    def get(self, mobile_id=None):
        # logged_in_user_email = get_jwt_identity()
        # logged_in_user = User.query.filter_by(email=logged_in_user_email).first()
        # print(f"Logged in user: {logged_in_user.name} with role: {logged_in_user.role}")

        if mobile_id is not None:
            mobile = Mobile.query.get(mobile_id)
            if not mobile:
                return {'message': f'Mobile not found with id {mobile_id}'}, 404
            mobile = {'id': mobile.id, 'name': mobile.name, 'color': mobile.color, 'ram': mobile.ram, 'price': mobile.price}
            return {'message': f"fetched mobile information with id {mobile_id}", 'mobile': mobile}, 200
        else:
            mobiles = Mobile.query.all() # querying all mobiles from database
            time.sleep(10)  # Simulate delay
            mobiles = [{'id': m.id, 'name': m.name, 'color': m.color, 'ram': m.ram, 'price': m.price} for m in mobiles]
            return {'message': "fetched all mobiles", 'mobiles': mobiles}, 200
        
    @jwt_required()
    def post(self, mobile_id=None):
        loggedin_user = User.query.filter_by(email=get_jwt_identity()).first()
        if loggedin_user.role != 'admin':
            return {'message': 'Only admin users can delete mobiles'}, 403

        if mobile_id:
            return {'message': 'Mobile ID should not be provided for POST requests'}, 400
        data = request.get_json()
        print('received data:',data)
        if not data.get('name') or not data.get('color') or not data.get('ram') or not data.get('price'):
            return {'message': "All fields must be non-empty"}, 400
        mobile = Mobile(name=data['name'], color=data['color'], ram=data['ram'], price=data['price'])
        db.session.add(mobile)   
        db.session.commit()
        mobile = {'id': mobile.id, 'name': mobile.name, 'color': mobile.color, 'ram': mobile.ram, 'price': mobile.price}
        return {'message': f"Mobile created successfully with id {mobile['id']}", 'mobile': mobile}, 201
    
    @jwt_required()
    def put(self, mobile_id=None):
        loggedin_user = User.query.filter_by(email=get_jwt_identity()).first()
        if loggedin_user.role != 'admin':
            return {'message': 'Only admin users can delete mobiles'}, 403

        if not mobile_id:
            return {'message': 'Mobile ID is required for PUT requests'}, 400
        mobile = Mobile.query.get(mobile_id)
        if not mobile:
            return {'message': f'Mobile not found with id {mobile_id}'}, 404
        data = request.get_json()
        print('received data:',data)
        if not data.get('name') or not data.get('color') or not data.get('ram') or not data.get('price'):
            return {'message': "All fields must be non-empty"}, 400
        mobile.name = data['name']
        mobile.color = data['color']
        mobile.ram = data['ram']
        mobile.price = data['price']
        db.session.commit()
        mobile = {'id': mobile.id, 'name': mobile.name, 'color': mobile.color, 'ram': mobile.ram, 'price': mobile.price}
        return {'message': f"Mobile updated successfully with id {mobile_id}", 'mobile': mobile}, 200
    
    @jwt_required()
    def delete(self, mobile_id=None):
        loggedin_user = User.query.filter_by(email=get_jwt_identity()).first()
        if loggedin_user.role != 'admin':
            return {'message': 'Only admin users can delete mobiles'}, 403

        if not mobile_id:
            return {'message': 'Mobile ID is required for DELETE requests'}, 400
        mobile = Mobile.query.get(mobile_id)
        if not mobile:
            return {'message': f'Mobile not found with id {mobile_id}'}, 404
        db.session.delete(mobile)
        db.session.commit()
        return {'message': f'Mobile with id {mobile_id} deleted successfully'}, 200
    
api.add_resource(MobileResource, '/mobiles', '/mobiles/<int:mobile_id>')

