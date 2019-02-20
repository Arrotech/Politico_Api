# from flask import make_response, jsonify, request, abort, Blueprint
# from app.api.v2.models.candidates_model import CandidatesModel
# from app.api.v2.models.users_model import UsersModel
# from app.api.v2.models.offices_model import OfficesModel
# from utils.validations import raise_error, check_candidates_keys, on_success
# from utils.authorization import admin_required
# import json
# from flask_jwt_extended import jwt_required, get_jwt_identity

# candidate_v2 = Blueprint('candidates_v2', __name__)


# class Candidates:
#     """Candidates enpoint to show interest in running for an office."""

#     @candidate_v2.route('/candidates/register', methods=['POST'])
#     @jwt_required
#     @admin_required
#     def post():
#         """A candidate can show interest to run for a seat."""

#         errors = check_candidates_keys(request)
#         if errors:
#             return raise_error(400, "Invalid {} key".format(', '.join(errors)))
#         details = request.get_json()
#         office = details['office']
#         user = details['user']

#         if OfficesModel().get_office_by_id(office_id):
#             if UsersModel().get_user_by_id(user_id):
#                 candidate = CandidatesModel().save(office, user)
#                 return on_success(201, "user promoted successfully")
#             return raise_error(404, "user does not exist")
#         return raise_error(404, "office does not exist")
