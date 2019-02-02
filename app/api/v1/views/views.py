from flask_restful import Resource
import json
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.models import ElectionsModel
from utils.validations import raise_error, check_party_keys

class Elections(Resource):
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
        
        res = ElectionsModel().save(name, hqAddress, logoUrl)
        return make_response(jsonify({
                "message" : "party created successfully!"
            }),201)


