from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.users_model import UsersModel
from utils.validations import raise_error, check_register_keys, is_valid_email, is_valid_url, on_success, is_valid_phone
import json
from werkzeug.security import check_password_hash, generate_password_hash
          
signup = Blueprint('signup',__name__)

class Register:
    """A user can create a new account."""
    
    @signup.route('/signup', methods=['POST'])
    def post():
        """Create new account."""

        errors = check_register_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        firstname = details['firstname']
        lastname = details['lastname']
        email = details['email']
        password = generate_password_hash(details['password'])
        phoneNumber = details['phoneNumber']
        passportUrl = details['passportUrl']
        role = details['role']

        if not is_valid_email(email):
            return raise_error(400,"Email is in the wrong format")
        if not is_valid_phone(phoneNumber):
            return raise_error(400,"phone number is in the wrong format")
        if details['firstname'].isalpha()== False:
            return raise_error(400,"firstname is in wrong format")
        if details['lastname'].isalpha()== False:
            return raise_error(400,"lastname is in wrong format")
        if details['role'].isalpha()== False:
            return raise_error(400,"role is in wrong format")
        if not is_valid_url(passportUrl):
            return raise_error(400,"passportUrl is in the wrong format")
        # if not is_valid_url(password):
        #     return raise_error(400,"password is in wrong format")

        user = UsersModel().save(firstname, lastname, email, password, phoneNumber, passportUrl, role)
        return on_success(201,"Account created successfully")

login = Blueprint('login', __name__)

class Login:
    """A user can sign in to their account."""

    @login.route('/login', methods=['POST'])
    def post():
        """Sign In a user"""

        details = request.get_json()

        email = details['email']
        password = details['password']

        user = UsersModel().get_email(email)

        if user:
            return make_response(jsonify({
                "message" : f"successfully logged in {email}",
            }), 200)
        if not user:
            return {'message': 'user not found'}, 404
