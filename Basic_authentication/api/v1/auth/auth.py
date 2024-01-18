#!/usr/bin/env python3

"""
Create a class called Auth
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ a class called Auth """

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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user method """
        return None
