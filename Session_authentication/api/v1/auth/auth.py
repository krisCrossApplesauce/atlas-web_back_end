#!/usr/bin/env python3

"""
Create a class called Auth
"""
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ a class called Auth """

    def __init__(self):
        """ initializes self """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth method """
        if path is None or excluded_paths is None or len(excluded_paths) is 0:
            return True
        if path[-1] != '/':
            path += '/'
        for ex_path in excluded_paths:
            if path == ex_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header method """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user method """
        return None

    def session_cookie(self, request=None):
        """ returns a cookie value from a request """
        if request is None:
            return None
        _my_session_id = request.cookies.get(os.getenv('SESSION_NAME'))
        return _my_session_id
