from flask import Flask, Blueprint, request, jsonify, make_response
from app.api.v1.views.party_views import party_v1 as v1
from app.api.v1.views.office_views import office_v2 as v2

def page_not_found(e):
	"""Capture Not Found error."""

	return make_response(jsonify({
		"status" : "not found",
		"message" : "url does not exist"
		}), 404)

def electoral_app():
	"""Create app."""

	app = Flask(__name__)
	app.register_blueprint(v1, url_prefix='/api/v1/')
	app.register_blueprint(v2, url_prefix='/api/v2/')
	app.register_error_handler(404, page_not_found)
	
	return app