#!/usr/bin/python3
'''Contains the index view for the API.'''
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns JSON indicating the status of the API."""
    return jsonify(status="OK")


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stat():
    """Returns JSON with the number of objects for each type."""
    try:
        statistics = {
            'amenities': storage.count('Amenity'),
            'cities': storage.count('City'),
            'places': storage.count('Place'),
            'reviews': storage.count('Review'),
            'states': storage.count('State'),
            'users': storage.count('User')
        }
        return jsonify(statistics)
    except Exception as e:
        return jsonify(error=str(e)), 500  # Return a 500 Internal Server Error on exception
