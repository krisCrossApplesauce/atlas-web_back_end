#!/usr/bin/env python3

"""
Create a class called BasicAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ basic auth """

    def __init__(self):
        """ initialize stuff """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ ridiculously long method name but ok I guess """
        if authorization_header is None \
            or type(authorization_header) is not str \
                or authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ returns the decoded value of a Base64 string """
        if base64_authorization_header is None \
                or type(base64_authorization_header) is not str:
            return None
        try:
            return base64_authorization_header.decode('utf-8')
        except:
            return None
