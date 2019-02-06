
import json
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.parties_model import PartiesModel, parties
from utils.validations import raise_error, check_party_keys

party_v1 = Blueprint('v1',__name__, url_prefix='/api/v1/')

class Party:
    """Creates a new political party."""

    @party_v1.route('/parties',methods=['POST'])
    def post():
        """Create a new political party."""
        
        errors = check_party_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        name = details['name']
        hqAddress = details['hqAddress']
        logoUrl = details['logoUrl']

        if not request.json:
            abort(400)
        if details['name'].isalpha()== False:
            return raise_error(400,"name is in wrong format")
        if details['hqAddress'].isalpha()== False:
            return raise_error(400,"hqAddress is in wrong format")
        if details['logoUrl'].isalpha()== False:
            return raise_error(400,"logoUrl is in wrong format")

        res = PartiesModel().save(name, hqAddress, logoUrl)
        return make_response(jsonify({
                "message" : "party created successfully!"
            }),201)

    @party_v1.route('/parties',methods=['GET'])
    def get_parties():
        """Fetch all the existing parties."""

        parties = {}
        parties = PartiesModel().get_all_parties()
        if parties:
            return make_response(jsonify({
            "message": "success",
            "parties": parties
            }),200)
        return make_response(jsonify({
            "message": "unavailable parties",
            "parties": parties
        }), 200)

    @party_v1.route('/parties/<int:party_id>',methods=['GET'])
    def get_party(party_id):
        """Fetch a specific political party."""

        party = PartiesModel().get_a_party(party_id)
        if party:
            return make_response(jsonify({
            "message": "success",
            "party" : party
            }),200)
        return make_response(jsonify({
            "status": "not found"
            }),404)

    @party_v1.route('/parties/<int:party_id>/delete',methods=['DELETE'])
    def delete_party(party_id):
        """Delete a specific party."""

        party = PartiesModel().get_a_party(party_id)
        if party:
            parties.remove(party)
            return make_response(jsonify({
                "message": "party deleted"
                }),200)
        return make_response(jsonify({
            "status": "not found"
            }),404)

    @party_v1.route('/parties/<int:party_id>/edit',methods=['PATCH'])
    def edit_party(party_id):
        """Edit a specific party."""

        details = request.get_json()
        party = PartiesModel().update_party(party_id, details)
        if party:
            return make_response(jsonify({
                "message": "party updated successfully"
                }),200)
        return make_response(jsonify({
            "status": "not found"
            }),404)