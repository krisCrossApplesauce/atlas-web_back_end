#!/usr/bin/env python3

"""
Create a class called BasicAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """ basic auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ ridiculously long method name but ok I guess """
        if authorization_header is None \
            or not isinstance(authorization_header, str) \
                or not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ returns the decoded value of a Base64 string """
        if base64_authorization_header is None \
                or not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(base64_authorization_header
                                    ).decode('utf-8')
        except(base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ returns the user email and password from the b64 decoded value """
        if decoded_base64_authorization_header is None \
            or not isinstance(decoded_base64_authorization_header, str) \
                or ":" not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ returns the User instance based on their email and password """
        if user_email is None or type(user_email) is not str \
                or user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            users = User.search({"email": user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ overloads Auth and retrieves the User instance for a request """
        if request is None:
            return None
        auth_head = self.authorization_header(request)
        ex_b64_auth_head = self.extract_base64_authorization_header(auth_head)
        dcode_b64_auth_head = self.decode_base64_authorization_header(
            ex_b64_auth_head)
        usr_email, usr_pwd = self.extract_user_credentials(dcode_b64_auth_head)
        user = self.user_object_from_credentials(usr_email, usr_pwd)
        return user
