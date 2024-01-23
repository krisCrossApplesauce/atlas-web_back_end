#!/usr/bin/env python3
"""
Create a class called SessionAuth that inherits from Auth
"""
from models.user import User
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ session auth """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a Session ID for a user_id """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns a User ID based on a Session ID """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ (overload) that returns a User instance based on a cookie value """
        cookie = self.session_cookie(request)
        if cookie is None:
            return None
        user_id = self.user_id_for_session_id(cookie)
        if user_id is None:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ deletes the user session/logout """
        if request is None:
            return False
        if not self.session_cookie(request):
            return False
        if not self.user_id_for_session_id():
