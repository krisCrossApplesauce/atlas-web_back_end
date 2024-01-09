#!/usr/bin/env python3

"""
Create a class called MRUCache
that inherits from BaseCaching and is a caching system:
    >  Same as LRUCache except MRU instead of LRU
    >  def put(self, key, item):
        >  If the number of items in dict is higher than self.MAX_ITEMS
            >  Must discard the most recently used item (MRU algorithm)
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ a caching system that uses a MRU algorithm """

    def __init__(self):
        """ inherits methods and properties from parent """
        super().__init__()

    def put(self, key, item):
        """ add an item in the cache, discarding most recently used item """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                disc_key = list(self.cache_data.keys())[self.MAX_ITEMS - 1]
                self.cache_data.pop(disc_key)
                print(f"DISCARD: {disc_key}")

    def get(self, key):
        """ get an item by key """
        if key in self.cache_data:
            self.cache_data[key] = self.cache_data.pop(key)
        return self.cache_data.get(key)
