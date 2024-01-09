#!/usr/bin/env python3

"""
Write a function named index_range
that takes two int args called page and page_size.

The func should return a tuple of size two
containing a start index and an end index
corresponding to the range of indexes to return in a list
for those particular pagination parameters.
"""

def index_range(page, page_size) -> tuple:
    """ a func that returns a tuple """
    return ((page - 1) * page_size, page * page_size)
