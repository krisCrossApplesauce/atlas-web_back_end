#!/usr/bin/env python3

"""
write a type-annotated function called sum_list
which takes a list of floats called input_list as an arg
and returns their sum as a float
"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """ returns sum of floats in a list """
    n: float = 0
    for i in input_list:
        n += i
    return n
