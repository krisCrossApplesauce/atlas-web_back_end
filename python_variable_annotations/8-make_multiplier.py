#!/usr/bin/env python3

"""
write a type-annotated function called make_multiplier
that takes a float called multiplier as an arg
and returns a function that multiplies a float by multiplier
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ returns a func that takes a float to be multiplied by multiplier """
    def infunc(f: float) -> float:
        return f * multiplier

    return infunc
