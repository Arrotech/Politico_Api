from flask import Flask, Blueprint, request, jsonify, make_response
from app.api.v1.views.party_views import party
from app.api.v1.views.office_views import office
from app.api.v1.views.user_views import user
from app.api.v1.views.candidates_views import candidate
from app.api.v1.views.voters_views import vote
from app.api.v1.views.petitions_views import petition


def page_not_found(e):
	"""Capture Not Found error."""
	
	return make_response(jsonify({
		"status" : "not found",
		"message" : "url does not exist"
		}), 404)

def method_not_allowed(e):
	"""Capture Not Found error."""
	
	return make_response(jsonify({
		"status" : "error",
		"message" : "method not allowed"
		}), 404)

def electoral_app():
	"""Create app."""

	app = Flask(__name__)
	app.register_blueprint(party, url_prefix='/api/v1/')
	app.register_blueprint(office, url_prefix='/api/v1/')
	app.register_blueprint(user, url_prefix='/api/v1/')
	app.register_blueprint(candidate, url_prefix='/api/v1/')
	app.register_blueprint(vote, url_prefix='/api/v1/')
	app.register_blueprint(petition, url_prefix='/api/v1/')

	app.register_error_handler(404, page_not_found)
	app.register_error_handler(405, method_not_allowed)
	
	return app