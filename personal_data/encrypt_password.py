#!/usr/bin/env python3

"""
Implement a func called hash_password
that expects one string arg named password
and returns a salted, hashed password, which is a byte str
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ hashes a password I guess """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)
