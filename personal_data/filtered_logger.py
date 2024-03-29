#!/usr/bin/env python3

"""
stuff that does things (wow!)
"""
import logging
import re
import typing


PII_FIELDS: tuple = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: typing.List[str],
                 redaction: str, message: str, separator: str) -> str:
    """ returns the log message obfuscated """
    for f in fields:
        message = re.sub(fr'{f}=.*?{separator}',
                         fr'{f}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        """ initializing stuff :P """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filter values in incoming log records using filter_datum """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """ does stuff """
    user_data = logging.getLogger(user_data)
    user_data.setLevel(logging.INFO)
    user_data.propagate = False
    h = logging.StreamHandler()
    h.setFormatter(RedactingFormatter())
    user_data.addHandler(h)
    return user_data
