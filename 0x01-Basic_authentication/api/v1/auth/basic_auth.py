#!/usr/bin/env python3
"""Module for Basic Authentication"""
from .auth import Auth
import re


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
