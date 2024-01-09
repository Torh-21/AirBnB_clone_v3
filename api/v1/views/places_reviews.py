#!/usr/bin/python3
""" Handles all default RESTFul API actions for Review object """
from api.vi.views import app_views
from flask import abort, jsonify, requests
from models import storage
from models.place import Place
from models.review import Review
from models.user import User


app_views.route('/places/<place_id>/reviews',
                method=['GET', 'POST'],
                strictslashes=False)


def place(place_id):
    """ Carries out GET and POST actions for this route """

    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    if method == "POST":
        user = storage.get(User, user_id)
        response = request.get_json()

        if user is None:
            abort(404)

        if response is None:
            abort(400, description="Not a JSON")

        if 'user_id' not in response.keys():
            abort(400, description="Missing user_id")

        if 'text' not in response.keys():
            abort(400, description='Missing text')

        response["place_id"] = place_id
        review = Review(**response)
        review.save()
        return (jsonify(review.to_dict())), 201

    reviews = [review.to_dict() for review in place.review]
    return (jsonify(reviews))


app_views.route('/reviews/<review_id>',
                method=['DELETE', 'GET', 'PUT'],
                strict_slashes=False)


def review_id(review_id):
    """ Performs HTTPs actions for this route """

    review = storage.get(Review, review_id)

    if review is None:
        abort(404)

    if method == "DELETE":
        review.delete()
        storage.save()
        return ("{}"), 200

    if method == "PUT":
        response = request.get_json()

        if response is None:
            abort(404, description="Not a JSON")

        for key, value in response.items():
            if key.endswith('ated_at') or key.endswith('id'):
                continue
            setattr(review, key, value)
        review.save()
    return (jsonify(review.to_dict())), 200
