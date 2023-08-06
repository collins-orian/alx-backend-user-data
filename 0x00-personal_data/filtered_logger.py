#!/usr/bin/env python3

'''This module is used to handle logs'''

import re


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscates specific field values in a log message.

    This function takes a log message as input and replaces
    the values of specified fields
    with a redaction string. The field names remain unchanged.

    Parameters:
        fields (list of str): A list of strings representing
        the names of fields to obfuscate.
        redaction (str): The string used to replace the
        values of the specified fields.
        message (str): The log message containing field-value
        pairs separated by a separator.
        separator (str): The character used to separate the
        field names and values in the log message.

    Returns:
        str: The obfuscated log message with specified field
        values replaced by the redaction string.
    """

    pattern = r'(' + separator + '|^)(' + \
        '|'.join(map(re.escape, fields)) + r')=([^' + separator + ']+)'
    return re.sub(pattern, r'\1\2=' + redaction, message)
