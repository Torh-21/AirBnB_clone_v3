#!/usr/bin/python3
"""Module __init__.py: create a blueprint"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.vi.views.users import *
from api.vi.views.places import *
from api.vi.views.places_reviews import *
