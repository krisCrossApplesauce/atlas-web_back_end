#!/usr/bin/env python3

"""
write a func called filter_datum that returns the log message obfuscated:
    > Arguments:
        >  fields: a list of strings representing all fields to obfuscate
        >  redaction: a string representing what the field will be obfuscated by
        >  message: a string representing the log line
        >  separator: a string representing which character is separating 
           all the fields in the log line (message)
    > The func should use a regex to replace occurrences of certain field values
    > filter_datum should be less than 5 lines long
      and use re.sub to perform the substitution with a single regex
"""
import re
import typing


def filter_datum(fields: typing.List[str],
                 redaction: str, message: str, separator: str) -> str:
    """ a function that does something """
    for f in fields:
        message = re.sub(fr'{f}=.*{separator}',
                         fr'{f}={redaction}{separator}', message)
    return message
