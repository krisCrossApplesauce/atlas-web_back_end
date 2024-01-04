#!/usr/bin/env python3

"""
write a type-annotated function called sum_mixed_list
which takes a list called mxd_lst of ints and floats
and returns their sum as a float
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """ returns sum of the numbers of a list as a float """
    n: float = 0
    for i in mxd_lst:
        n += i
    return n
