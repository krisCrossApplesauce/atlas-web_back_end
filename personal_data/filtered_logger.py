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


def filter_datum(fields, redaction, message, separator):
    """ a function that does something """
    split_mess = re.split(separator, message)
    reverse_fields = []
    for i in split_mess:
        for iii in fields:
            if re.findall(fr'{iii}=', i) is not []:
                reverse_fields.append(re.sub(fr'{iii}=', "", i))
    string = message
    for ii in reverse_fields:
        string = re.sub(fr'{ii}', redaction, message)
    return string
