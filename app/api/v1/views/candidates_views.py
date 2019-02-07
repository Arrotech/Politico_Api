from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.candidates_model import CandidatesModel, candidates
from utils.validations import raise_error, check_candidates_keys, on_success
import json
          
candidate_v4 = Blueprint('v4',__name__, url_prefix='/api/v4/')

class Candidates:
    """Candidates enpoint to show interest in running for an office."""
    
    @candidate_v4.route('/candidates', methods=['POST'])
    def post():
        """A candidate can show interest to run for a seat."""

        errors = check_candidates_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        office = details['office']
        party = details['party']
        candidate = details['candidate']

        if details['office'].isalpha()== False:
            return raise_error(400,"office is in wrong format")
        if details['party'].isalpha()== False:
            return raise_error(400,"party is in wrong format")
        if details['candidate'].isalpha()== False:
            return raise_error(400,"candidate is in wrong format")
        candidate = CandidatesModel().save(office, party, candidate)
        return on_success(201,"interest created successfully")