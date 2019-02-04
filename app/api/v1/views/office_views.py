
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.offices_model import OfficesModel, offices
from utils.validations import raise_error, check_office_keys
import json

office_v2 = Blueprint('v2',__name__, url_prefix='/api/v2/')

class Office:
    """Creates a new government office."""

    @office_v2.route('/offices',methods=['POST'])
    def post():
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
            return raise_error(400,"category is in wrong format")
        if details['name'].isalpha()== False:
            return raise_error(400,"name is in wrong format")
        
        res = OfficesModel().save(category, name)
        return make_response(jsonify({
                "message" : "office created successfully!"
            }),201)
        
    @office_v2.route('/offices',methods=['GET'])
    def get_offices():
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

    @office_v2.route('/offices/<int:office_id>',methods=['GET'])
    def get_office(office_id):
        """Fetch a specific political office."""

        office = OfficesModel().get_an_office(office_id)
        if office:
            return make_response(jsonify({
            "message": "success",
            "office" : office
            }),200)
        return make_response(jsonify({
            "status": "not found"
            }),404)

    @office_v2.route('/offices/<int:office_id>/delete',methods=['DELETE'])
    def delete(office_id):
        """Delete a specific office."""

        office = OfficesModel().get_an_office(office_id)
        if office:
            offices.remove(office)
            return make_response(jsonify({
                "message": "office deleted"
                }),200)
        return make_response(jsonify({
            "status": "not found"
            }),404)