from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.offices_model import OfficesModel
from utils.validations import raise_error, check_office_keys, on_success, office_restrictions
import json

office_v2 = Blueprint('office_v2', __name__)


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
        if(office_restrictions(category) is False):
            return raise_error(400, "select from state, local, federal or legislative")
        if OfficesModel().get_office_name(name):
            return raise_error(400, "Office with that name already exists")

        res = OfficesModel().save(category, name)
        return jsonify({
            "message": "office created successfully!",
            }), 201

    @office_v2.route('/offices', methods=['GET'])
    def get_offices():
        '''Fetch all the existing offices.'''

        return make_response(jsonify({
            "message": "success",
            "offices": json.loads(OfficesModel().get_offices())
            }), 200)

    @office_v2.route('/offices/<int:office_id>', methods=['GET'])
    def get_office(office_id):
        """Fetch a specific political office."""

        office = OfficesModel().get_office_by_id(office_id)
        office = json.loads(office)
        if office:
            return make_response(jsonify({
                "message": "success",
                "office": office
                }), 200)
        return make_response(jsonify({
            "status": "not found"
            }), 404)
