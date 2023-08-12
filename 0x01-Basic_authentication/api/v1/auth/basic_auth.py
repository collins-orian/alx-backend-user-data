#!/usr/bin/env python3
"""Module for Basic Authentication"""
from .auth import Auth
from models.user import User
import re
import base64
import binascii
from typing import TypeVar, Tuple


class BasicAuth(Auth):
    """This class handles Basic Authentication"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header
        for a Basic Authentication.
        """
        # checks if the authorization header is a string
        if type(authorization_header) == str:
            # uses regular expression to extract the base64 encoded string
            pattern = r'Basic (?P<token>.+)'
            #  checks if the authorization header contains a valid token
            part_match = re.fullmatch(pattern, authorization_header.strip())
            # if the part_match returns true, the return the token
            if part_match is not None:
                return part_match.group('token')
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """This method returns the decoded value of a Base64 string"""
        if type(base64_authorization_header) == str:
            try:
                res = base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                )
                return res.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """This method returns the user email and password
        from the Base64 decoded value"""
        if type(decoded_base64_authorization_header) == str:
            pattern = r'(?P<user>[^:]+):(?P<password>.+)'
            field_match = re.fullmatch(
                pattern,
                decoded_base64_authorization_header.strip(),
            )
            if field_match is not None:
                user = field_match.group('user')
                password = field_match.group('password')
                return user, password
        return None, None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """This method  that returns the User instance based
        on his email and password."""
        if type(user_email) == str and type(user_pwd) == str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None
