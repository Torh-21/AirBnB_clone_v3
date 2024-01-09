#!/usr/bin/python3
"""
Module: Initializes a Flask app for the HBNB API.

This module sets up a Flask app, configures CORS, registers blueprints, and
defines error handling and teardown functions.
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
import os


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(e):
    """Handles the 404 error page.

    Args:
        e: The exception object.

    Returns:
        JSON response with a 404 status code.
    """
    return jsonify(error='Not found'), 404


@app.teardown_appcontext
def tear_down(Exception):
    """closes the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=os.getenv('HBNB_API_PORT', '5000'),
            threaded=True)
