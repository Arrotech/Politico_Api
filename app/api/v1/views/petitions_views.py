from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.petitions_model import PetitionsModel, petitions
from utils.validations import raise_error, check_petitions_keys, on_success, is_valid_date
import json
          
petition_v6 = Blueprint('v6',__name__, url_prefix='/api/v6/')

class Petition:
    """A user can file a petition."""
    
    @petition_v6.route('/petitions', methods=['POST'])
    def post():
        """A user can file a petition."""

        errors = check_petitions_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        createdOn = details['createdOn']
        createdBy = details['createdBy']
        office = details['office']
        body = details['body']

        if details['office'].isalpha()== False:
            return raise_error(400,"office is in wrong format")
        if not is_valid_date(createdOn):
            return raise_error(400,"createdOn is in the wrong format")
        if details['createdBy'].isalpha()== False:
            return raise_error(400,"createdBy is in wrong format")
        petition = PetitionsModel().save(createdOn, createdBy, office, body)
        return on_success(201,"petition filed successfully")