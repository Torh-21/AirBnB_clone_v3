#!/usr/bin/python3
""" Handles default RESTFul API actions for the Place objects """
from app.v1.views import app_views
from flask import abort, jsonify, requests
from models import storage
from models.place import Place
from models.state import State
from models.user import User

app_views.route('/cities/<city_id>/places',
                method=['GET', 'POST'],
                strict_slashes=False)


def place(city_id):
    """ Handles GET and POST HTTP operations for this route """
    if request.method == 'POST':
        response = request.get_json()
        city = storage.get('City', city_id)
        user = storage.get('User', user_id)

        if city is None:
            abort(404)

        if user is None:
            abort(404)

        if response is None:
            abort(400, description="Not a JSON")

        if 'user_id' not in response.keys():
            abort(400, description="Missing user_id")

        if 'name' not in response.keys():
            abort(400, description="Missing name")

        response['city_id'] = city_id
        place = Place(**response)
        place.save()
        return (jsonify(place.to_dict())), 201

    places = []
    for place in city.places:
        places.append(place.to_dict())
    return jsonify(places)


app_view.route('/places/<place_id>',
               method=['DELETE', 'POST', 'PUT'],
               strict_slashes=False)


def place_id(place_id):
    """ Handles some HTTPS operations for this route """

    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    if method == "DELETE":
        place.delete()
        storage.save()
        return ("{}"), 200

    if method == "PUT":
        response = requests.get_json()

        if response is None:
            abort(400, description="Not a JSON")
        for key, value in response.items():
            if key.endswith('ated_at') or key.endswith('id'):
                continue
            setattr(place, key, value)
        place.save()

    return (jsonify(place.to_dict()))
