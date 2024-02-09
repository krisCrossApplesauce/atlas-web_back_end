#!/usr/bin/env python3
""" Cache class """
import redis
import typing
import uuid


class Cache():
    """ Cache class """

    def __init__(self):
        """ initializes an instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """ takes a data arg and returns a str """
        key = str(uuid.uuid4())
        self._redis[key] = data
        return key
