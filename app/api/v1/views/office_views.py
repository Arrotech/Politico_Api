from flask_restful import Resource
import json
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.offices_model import OfficesModel, offices
from utils.validations import raise_error, check_office_keys

class CreateOffice(Resource):
    """Creates a new government office."""

    def post(self):
        """Create a new government office."""

        errors = check_office_keys(request)
        if errors:
            return raise_error(400,"Invalid {} key".format(', '.join(errors)))

        details = request.get_json()
        category = details['category']
        name = details['name']

        if not request.json:
            abort(400)
        if details['category'].isalpha()== False:
            return make_response(jsonify({"message": "category is in wrong format"}),400)
        if details['name'].isalpha()== False:
            return make_response(jsonify({"message": "name is in wrong format"}),400)
        
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