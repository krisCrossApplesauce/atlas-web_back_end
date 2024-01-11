#!/usr/bin/env python3

"""
Deletion-resilient hypermedia pagination

Implement a get_hyper_index method with two int args:
index, with None as its default value
and page_size, with a default value of 10.

The method should return a dictionary with the following key-value pairs:
    >  index: the current start index of the return page,
       aka the index of the first item in the current page
    >  next_index: the next index to query with,
       aka the index of the first item on the next page
       (the index of the item right after the last item on the current page)
    >  page_size: the current page size
    >  data: the actual page of the dataset

Requirements/Behavior:
    >  Use assert to verify that index is in a valid range
    >  Returns rows 0 through (page_size - 1) if the user queries index 0
    >  Maintains the page that the rows are on, even if rows get deleted
"""
import csv
import math
from typing import List
from typing import Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ initializes stuff """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ does stuff """
        hyper = {}
        data = self.__indexed_dataset
        not_last = index <= len(data) - page_size

        assert index < len(data)

        hyper['index'] = index
        hyper['data'] = []
        i = index
        while i <= index + page_size \
                and len(hyper['data']) < page_size and i < len(data):
            # for i in range(index, index + page_size):
            if i in data:
                hyper['data'].append(data[i])
            i += 1
        hyper['page_size'] = page_size if not_last else len(data) % page_size
        hyper['next_index'] = index + page_size

        return hyper
