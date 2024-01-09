#!/usr/bin/python3
""" Handles all default RESTFul API actions """
from api.v1.views import app_views
from models.user import User
from models import storage
from flask import abort, jsonify, request

app_views.route('/users',
                methods=['GET', 'POST'],
                strict_slashes=False)


def users():
    """ Returns all user object """
    if request.method == 'POST':
        response = request.get_json()

        if not response:
            abort(400, description="Not a JSON")

        if 'email' not in response.keys():
            abort(400, description="Missing email")

        if 'password' not in response.keys():
            abort(400, description='Missing password')
        newUser = User(**response)
        newUser.save()
        return (newUser.to_dict()), 201

    users = [user.to_dict() for user in storage.all('State').values()]
    return jsonify(users)


app_views.route('/city/<user_id>',
                methods=['GET', 'DELETE', 'PUT'],
                strict_slashes=False)


def user_id(user_id):
    """ Carries out HTTPs operations based on the user id """

    user = storage.get("User", user_id)
    if not user:
        abort(404)

    if request.method == 'DELETE':
        user.delete()
        storage.save()
        return ('{}'), 200

    if request.method == 'PUT':
        response = requests.get_json()

        if response is None:
            abort('400', description="Not a JSON")
        for key, value in response.item():
            if key.endswith('ated_at') or k == 'id':
                continue
            setattr(user, key, value)
        user.save()

    return (jsonify(user.to_dict()))
