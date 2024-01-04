#!/usr/bin/env python3

"""
write a type-annotated function called to_kv
that takes a string called k and an int/float called v as args
and returns a tuple
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    a func that returns a tuple,
    the first element is the str k,
    the second element is a float that is the square of v
    """
    return (k, v ** 2)
