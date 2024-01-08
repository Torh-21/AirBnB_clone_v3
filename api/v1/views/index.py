#!/usr/bin/python3
"""Module index.py: initializing the flask app"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    """returns the status"""
    return jsonify(status='OK')
