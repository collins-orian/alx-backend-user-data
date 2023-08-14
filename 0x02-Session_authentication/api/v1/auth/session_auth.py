#!/usr/bin/env python3
"""Module for Session Authentication"""
from .auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """This class handles Session Authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        if type(user_id) == str:
            sess_id = str(uuid4())
            self.user_id_by_session_id[sess_id] = user_id
            return sess_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """This method returns a User ID based on a Session ID"""
        if type(session_id) == str:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """This method returns a User instance based on a cookie value"""
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)

    def destroy_session(self, request=None):
        """Destroys an authenticated session.
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if (request is None or session_id is None) or user_id is None:
            return False
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]
        return True
