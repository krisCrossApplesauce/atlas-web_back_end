#!/usr/bin/env python3
""" Cache class """
from functools import wraps
import redis
import uuid
from typing import Callable, Union


def count_calls(method: Callable) -> Callable:
    """ a decorator??? to count the number of times methods are called """
    @wraps(method)
    def func(self, *args):
        self._redis.incr(method.__qualname__)
        return method(self, *args)

    return func


def call_history(method: Callable) -> Callable:
    """ a decorator! to store the history of inputs and outputs for a func """
    @wraps(method)
    def func(self, *args):
        input = f"{method.__qualname__}:inputs"
        self._redis.rpush(input, str(args))
        output = f"{method.__qualname__}:outputs"
        result = method(self, *args)
        self._redis.rpush(output, result)
        return result

    return func


def replay(method: Callable):
    """ displays the history of calls of a particular func """
    self = method.__self__
    inputs = self._redis.lrange(f"{method.__qualname__}:inputs", 0, -1)
    outputs = self._redis.lrange(f"{method.__qualname__}:outputs", 0, -1)
    history = zip(inputs, outputs)
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input, output in history:
        print(f"{method.__qualname__}(*{input}) -> {output}")


class Cache():
    """ Cache class """

    def __init__(self):
        """ initializes an instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
