#!/usr/bin/env python3

"""
Replicate code from the prev task

Implement a get_hyper method
that takes the same args (and defaults) as get_page
and returns a dict containing the following key-value pairs:
    >  page_size: the length of the returned dataset page
    >  page: the current page number
    >  data: the dataset page (equivalent to return from prev task)
    >  next_page: number of the next page, None if no next page
    >  prev_page: number of the prev page, None if no prev page
    >  total_pages: the total number of pages in the dataset as an int

Make sure to reuse get_page in your implementation
"""
import csv
import math
from typing import List
from typing import Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ returns a dict """
        hyper = {}
        data = self.dataset()
        page_range = index_range(page, page_size)
        not_last = len(data) > page_range[1]

        hyper['page_size'] = page_size if not_last else len(data) % page_size
        hyper['page'] = page
        hyper['data'] = self.get_page(page, page_size)
        hyper['next_page'] = page + 1 if not_last else None
        hyper['prev_page'] = page - 1 if page_range[0] > 0 else None
        hyper['total_pages'] = math.ceil(len(data) / page_size)

        return hyper
