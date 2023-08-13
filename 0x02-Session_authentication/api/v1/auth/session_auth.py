#!/usr/bin/env python3
"""Module for Session Authentication"""
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """This class handles Session Authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        if type(user_id) == str:
            sess_id = str(uuid4())
            self.user_id_by_session_id[sess_id] = user_id
            return sess_id
