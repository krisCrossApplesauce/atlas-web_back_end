#!/usr/bin/env python3

"""
Copy index_range from the prev task and the following class into your code.

In the given class, implement a method named get_page
that takes two int args:
one called page, with a default value of 1
and another called page_size, with a default value of 10
    >  Must use the csv file (Popular_Baby_Names.csv)
    >  Use assert to verify that both args are ints greater than 0
    >  Use index_range to find the correct indexes
       to paginate the dataset correctly
       and return the appropriate page of the dataset
       (i.e. the correct list of rows)
    >  If the input args are out of range for the dataset,
        an empty list should be returned
"""
import csv
import math
from typing import List


def index_range(page, page_size) -> tuple:
    """ a func that returns a tuple """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """ Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ initializing whatever, I don't care,
        it's stupid that this wasn't already documented >,'/
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ returns a page """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        data = self.dataset()
        page_range = index_range(page, page_size)
        end_range = page_range[1] if len(data) > page_range[1] else len(data)
        if len(data) >= page_range[0]:
            return [data[i] for i in range(page_range[0], end_range)]
        return []
