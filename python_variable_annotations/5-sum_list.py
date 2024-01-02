#!/usr/bin/env python3

"""
write a type-annotated function called sum_list
which takes a list of floats called input_list as an arg
and returns their sum as a float
"""


def sum_list(input_list: float) -> float:
    """ returns sum of floats in a list """
    n: float = 0
    i = 1
    while input_list[i]:
        n += input_list[i]
    return n
