#!/usr/bin/env python3

"""
annotate the given function's parameters and return values
with the appropriate types
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) \
        -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """ return whatever, I don't care, it's not my code """
    return [(i, len(i)) for i in lst]
