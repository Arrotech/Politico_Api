from flask import Flask, Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from app.api.v1.views.views import CreateParty, GetParties, GetParty, CreateOffice

def page_not_found(e):
	"""Capture Not Found error."""

	return make_response(jsonify({
		"status" : "not found",
		"message" : "url does not exist"
		}), 404)

def electoral_app():
	"""Create app."""

	app = Flask(__name__)
	api = Api(app)

	api.add_resource(CreateParty, '/api/v1/parties')
	api.add_resource(GetParties, '/api/v1/parties')
	api.add_resource(GetParty, '/api/v1/parties/<int:party_id>')
	api.add_resource(CreateOffice, '/api/v1/offices')
	app.register_error_handler(404, page_not_found)
	
	return app