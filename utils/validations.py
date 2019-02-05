import re
from flask import jsonify, make_response

def check_party_keys(request):
    """Check if the key values are correct."""

    res_keys = ['name', 'hqAddress', 'logoUrl']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_voters_keys(request):
    """Check if the key values are correct."""

    res_keys = ['createdOn', 'createdBy', 'office', 'candidate']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_candidates_keys(request):
    """Check if the key values are correct."""

    res_keys = ['office', 'party', 'candidate']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_register_keys(request):
    """Check if the key values are correct."""

    res_keys = ['firstname', 'lastname', 'othername', 'email', 'phoneNumber', 'passportUrl', 'role']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_office_keys(request):
    """Check if the key values are correct."""

    res_keys = ['category', 'name']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def raise_error(status, msg):
    """Handles error messages."""
  
    return make_response(jsonify({
            "status": "error",
            "message": msg
        }), status)

