from flask_restful import Resource
import json
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.models import PartiesModel, OfficesModel, parties, offices
from utils.validations import raise_error, check_party_keys, check_office_keys

class CreateParty(Resource):
    """Creates a new political party."""

    def post(self):
        """Create a new political party."""

        details = request.get_json()
        errors = check_party_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))

        name = details['name']
        hqAddress = details['hqAddress']
        logoUrl = details['logoUrl']
        
        res = PartiesModel().save(name, hqAddress, logoUrl)
        return make_response(jsonify({
                "message" : "party created successfully!"
            }),201)


class GetParties(Resource):
    """Fetch all parties."""

    def get(self):
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

class GetParty(Resource):
    """Fetch a specific party."""

    def get(self, party_id):
        """Fetch a specific political party."""

        party = PartiesModel().get_party_by_id(party_id)
        if party:
            return make_response(jsonify({
            "message": "success",
            "party" : party
            }),200)
        return make_response(jsonify({
            "status": "not found"
            }),404)

class DeleteParty(Resource):
    """Delete a specific party."""

    def delete(self, party_id):
        """Delete a specific party."""

        party = PartiesModel().get_party_by_id(party_id)
        if party:
            parties.remove(party)
            return make_response(jsonify({
                "message": "party deleted"
                }),200)
        return make_response(jsonify({
            "status": "not found"
            }),404)

class CreateOffice(Resource):
    """Creates a new government office."""

    def post(self):
        """Create a new government office."""

        details = request.get_json()
        errors = check_office_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))

        category = details['category']
        name = details['name']
        
        res = OfficesModel().save(category, name)
        return make_response(jsonify({
                "message" : "office created successfully!"
            }),201)
        
class GetOffices(Resource):
    '''Fetch all offices.'''

    def get(self):
        '''Fetch all the existing offices.'''

        empty_offices = {}
        offices = OfficesModel().get_all_offices()
        if offices:
            return make_response(jsonify({
            "message": "success",
            "offices": offices
            }),200)
        return make_response(jsonify({
            "message": "success",
            "offices": empty_offices
            }),200)

class GetOffice(Resource):
    """Fetch a specific office."""

    def get(self, office_id):
        """Fetch a specific political office."""

        office = OfficesModel().get_office_by_id(office_id)
        if office:
            return make_response(jsonify({
            "message": "success",
            "office" : office
            }),200)
        return make_response(jsonify({
            "status": "not found"
            }),404)

class DeleteOffice(Resource):
    """Delete a specific office."""

    def delete(self, office_id):
        """Delete a specific office."""

        office = OfficesModel().get_office_by_id(office_id)
        if office:
            offices.remove(office)
            return make_response(jsonify({
                "message": "office deleted"
                }),200)
        return make_response(jsonify({
            "status": "not found"
            }),404)