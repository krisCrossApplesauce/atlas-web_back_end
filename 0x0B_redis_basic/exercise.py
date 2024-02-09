#!/usr/bin/env python3
""" Cache class """
from functools import wraps
import redis
import uuid
from typing import Callable, Union


def count_calls(method: Callable) -> Callable:
    """ a decorator??? to count the number of times methods are called """
    @wraps(method)
    def func(self, data):
        self._redis.incr(method.__qualname__)
        return method(self, data)

    return func


class Cache():
    """ Cache class """

    def __init__(self):
        """ initializes an instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ takes a data arg and returns a str """
        key = str(uuid.uuid4())
        self._redis[key] = data
        return key

    def get(self, key: str, fn: Callable = None):
        """ converts data back to desired form """
        b_data = self._redis.get(key)
        if fn and callable(fn):
            return fn(b_data)
        return b_data

    def get_str(self, key: str):
        """ automatically parametrize get method w/ str conversion func """
        return self.get(key, str)

    def get_int(self, key: str):
        """ automatically parametrize get method w/ int conversion func """
        return self.get(key, int)
