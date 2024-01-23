#!/usr/bin/env python3
""" handles all routes for the Session authentication """
from api.v1.views import app_views
from flask import request, jsonify, make_response
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def login():
    """ it's not really telling me what this is supposed to do """
    email = request.form.get("email")
    if email is None:
        return jsonify({ "error": "email missing" }), 400
    password = request.form.get("password")
    if password is None:
        return jsonify({ "error": "password missing" }), 400

    user = User.search({"email": email})
    if user is None:
        return jsonify({ "error": "no user found for this email" }), 404
    if not user.is_valid_password(password):
        return jsonify({ "error": "wrong password" }), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = make_response(jsonify(user.to_json()))
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return response
