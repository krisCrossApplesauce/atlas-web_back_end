#!/usr/bin/env python3
""" handles all routes for the Session authentication """
from api.v1.views import app_views
from flask import request, jsonify, make_response, abort
from models.user import User
from api.v1.app import auth
import os


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def login():
    """ it's not really telling me what this is supposed to do """
    email = request.form.get("email")
    if not email or email is None:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get("password")
    if not password or password is None:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users or users is None:
        return jsonify({"error": "no user found for this email"}), 404
    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = make_response(jsonify(user.to_json()))
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return response


@app_views.route('/api/v1/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ it logs out, deleting the session id """
    destroyed = auth.destroy_session(request)
    if not destroyed:
        abort(404)
    return jsonify({}), 200
