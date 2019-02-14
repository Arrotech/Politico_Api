from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.voters_model import VotersModel
from utils.validations import raise_error, \
    check_voters_keys2, on_success, is_valid_date
import json
vote_v2= Blueprint('votes_v2', __name__)


class Vote:
    """A user can vote his/her candidate of choice."""

    @vote_v2.route('/voters', methods=['POST'])
    def post():
        """A user can vote his/her candidate of choice."""

        errors = check_voters_keys2(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        createdBy = details['createdBy']
        office = details['office']
        candidate = details['candidate']

        if details['office'].isalpha() is False \
                or details['candidate'].isalpha() is False \
                or details['createdBy'].isalpha() is False:
            return raise_error(400, "input is in wrong format")
            
        voter = VotersModel().save(createdBy, office, candidate)
        return on_success(201, "voted successfully")
