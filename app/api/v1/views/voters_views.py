from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.voters_model import VotersModel, voters
from utils.validations import raise_error, check_voters_keys
import json
          
vote_v5 = Blueprint('v5',__name__, url_prefix='/api/v5/')

class Vote:
    """A user can vote his/her candidate of choice."""
    
    @vote_v5.route('/voters', methods=['POST'])
    def post():
        """A user can vote his/her candidate of choice."""

        errors = check_voters_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        createdOn = details['createdOn']
        createdBy = details['createdBy']
        office = details['office']
        candidate = details['candidate']

        voter = VotersModel().save(createdOn, createdBy, office, candidate)
        return make_response(jsonify({
            'message': 'voted successfully'
            }),201)