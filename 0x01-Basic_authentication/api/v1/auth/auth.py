#!/usr/bin/env python3
"""Module for Authentication"""
from flask import request as req
from typing import List, TypeVar


class Auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """gets the authorization header from the request"""
        if request is not None:
            return req.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """gets the current user from the request"""
        if request is not None:
            return req.headers.get('Authorization', None)
        return None
