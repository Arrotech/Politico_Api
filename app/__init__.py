from flask import Flask, Blueprint, request, jsonify, make_response
from app.api.v1.views.party_views import party
from app.api.v1.views.office_views import office
from app.api.v1.views.user_views import user
from app.api.v1.views.candidates_views import candidate
from app.api.v1.views.voters_views import vote
from app.api.v1.views.petitions_views import petition
from app.api.v2.views.auth_views import signup, login
from app.api.v2.views.office import office_v2
from app.api.v2.views.vote import vote_v2
from app.api.v2.views.petition import petition_v2
from app.api.v2.views.party_views import party_v2
from app.config import app_config
import os
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity


def page_not_found(e):
    """Capture Not Found error."""

    return make_response(jsonify({
        "status": "not found",
        "message": "url does not exist"
    }), 404)


def method_not_allowed(e):
    """Capture Not Found error."""

    return make_response(jsonify({
        "status": "error",
        "message": "method not allowed"
    }), 405)

# def method_not_allowed(e):
#     """Capture Not Found error."""

#     return make_response(jsonify({
#         "status": "500",
#         "message": "content type should be json"
#     }), 500)

def electoral_app(config_name):
    """Create app."""

    app = Flask(__name__)

    app.config.from_pyfile('config.py')
    app.config["SECRET_KEY"] = 'thisisarrotech'
    jwt = JWTManager(app)
    
    app.register_blueprint(party, url_prefix='/api/v1/')
    app.register_blueprint(office, url_prefix='/api/v1/')
    app.register_blueprint(user, url_prefix='/api/v1/')
    app.register_blueprint(candidate, url_prefix='/api/v1/')
    app.register_blueprint(vote, url_prefix='/api/v1/')
    app.register_blueprint(petition, url_prefix='/api/v1/')
    app.register_blueprint(signup, url_prefix='/api/v2/auth/')
    app.register_blueprint(login, url_prefix='/api/v2/auth/')
    app.register_blueprint(office_v2, url_prefix='/api/v2/')
    app.register_blueprint(vote_v2, url_prefix='/api/v2/')
    app.register_blueprint(petition_v2, url_prefix='/api/v2/')
    app.register_blueprint(party_v2, url_prefix='/api/v2/')

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, method_not_allowed)
    return app
