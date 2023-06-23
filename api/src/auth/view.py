from flask_restx import Namespace,Resource, fields
from flask import request
# from ..models.users import User
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import Conflict,BadRequest
from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token,jwt_required,get_jwt_identity

auth_namespace=Namespace('auth', description='Namespace for authentication')
@auth_namespace.route('/signup')
class SignUp(Resource):


    def post(self):
        """
            Create a new user account
        """

       
@auth_namespace.route('/login')
class Login(Resource):

    def post(self):
        """
            Generate a JWT
        """
        
@auth_namespace.route('/refresh')
class Refresh(Resource):

    def post(self):
        """
            Generate a refresh JWT
        """