from flask import Flask, Blueprint, request, jsonify, make_response
from app.api.v1.views.party_views import party_v1 as v1
from app.api.v1.views.office_views import office_v2 as v2
from app.api.v1.views.user_views import user_v3 as v3
from app.api.v1.views.candidates_views import candidate_v4 as v4
from app.api.v1.views.voters_views import vote_v5 as v5
from app.api.v1.views.petitions_views import petition_v6 as v6


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
	app.register_blueprint(v3, url_prefix='/api/v3/')
	app.register_blueprint(v4, url_prefix='/api/v4/')
	app.register_blueprint(v5, url_prefix='/api/v5/')
	app.register_blueprint(v6, url_prefix='/api/v6/')
	app.register_error_handler(404, page_not_found)
	
	return app