#!/usr/bin/env python3
"""Module for Authentication"""
from flask import request as req
from typing import List, TypeVar
import re


class Auth:
    '''This class is the template for all authentication
    system you will implement.'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication."""
        if path is not None or excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """gets the authorization header from the request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """gets the current user from the request"""
        return None
