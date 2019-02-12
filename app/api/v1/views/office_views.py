
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.offices_model import OfficesModel, offices
from utils.validations import raise_error, check_office_keys, on_success
import json
office_v2 = Blueprint('v2', __name__, url_prefix='/api/v2/')


class Office:
    """Creates a new government office."""

    @office_v2.route('/offices', methods=['POST'])
    def post():
        """Create a new government office."""

        errors = check_office_keys(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        category = details['category']
        name = details['name']

        if details['category'].isalpha() \
                is False or details['name'].isalpha() \
                is False:
            return raise_error(400, "input is in wrong format")

        res = OfficesModel().save(category, name)
        return jsonify({
            "message": "office created successfully!",
            "id": len(offices)
            }), 201

    @office_v2.route('/offices', methods=['GET'])
    def get_offices():
        '''Fetch all the existing offices.'''

        return make_response(jsonify({
            "message": "success",
            "offices": OfficesModel().get_all_offices()
            }), 200)

    @office_v2.route('/offices/<int:office_id>', methods=['GET'])
    def get_office(office_id):
        """Fetch a specific political office."""

        office = OfficesModel().get_an_office(office_id)
        if office:
            return make_response(jsonify({
                "message": "success",
                "office": office
                }), 200)
        return make_response(jsonify({
            "status": "not found"
            }), 404)

    @office_v2.route('/offices/<int:office_id>/delete', methods=['DELETE'])
    def delete(office_id):
        """Delete a specific office."""

        office = OfficesModel().get_an_office(office_id)
        if office:
            offices.remove(office)
            return make_response(jsonify({
                "message": "office deleted"
                }), 200)
        return make_response(jsonify({
            "status": "not found"
            }), 404)

    @office_v2.route('/offices/<int:office_id>/edit', methods=['PATCH'])
    def edit_office(office_id):
        """Edit a specific office."""

        details = request.get_json()
        office = OfficesModel().update_office(office_id, details)
        if office:
            return make_response(jsonify({
                "message": "office updated successfully"
                }), 200)
        return make_response(jsonify({
            "status": "not found"
            }), 404)
