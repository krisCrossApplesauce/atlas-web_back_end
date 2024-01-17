#!/usr/bin/env python3

"""
Implement a func called hash_password
that expects one string arg named password
and returns a salted, hashed password, which is a byte str

Implement a func called is_valid
that expects two args and returns a boolean
Args:
    >  hashed_password: bytes type
    >  password: string type
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ returns a salted, hashed password """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)

def is_valid(hashed_password: bytes, password: str):
    """ checks if given password is valid """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
