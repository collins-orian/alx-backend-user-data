#!/usr/bin/env python3
"""Module for Basic Authentication"""
from .auth import Auth
import re
import base64
import binascii


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
        """that returns the decoded value of a Base64 string"""
        if type(base64_authorization_header) == str:
            try:
                res = base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                )
                return res.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None
