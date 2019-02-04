from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.users_model import UsersModel, users
from utils.validations import raise_error, check_register_keys 
import json
          
user_v3 = Blueprint('v3',__name__, url_prefix='/api/v3/')

class Register:
    """A user can create a new account."""
    
    @user_v3.route('/users', methods=['POST'])
    def post():
        """Create new account."""

        errors = check_register_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        firstname = details['firstname']
        lastname = details['lastname']
        othername = details['othername']
        email = details['email']
        phoneNumber = details['phoneNumber']
        passportUrl = details['passportUrl']
        role = details['role']

        user = UsersModel().save(firstname, lastname, othername, email, phoneNumber, passportUrl, role)
        return make_response(jsonify({
            'message': 'Account created successfully'
            }),201)