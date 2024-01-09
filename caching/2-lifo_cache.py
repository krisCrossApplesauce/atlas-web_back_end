#!/usr/bin/env python3

"""
Create a class called LIFOCache
that inherits from BaseCaching and is a caching system:
    >  Same as FIFOCache except LIFO instead of FIFO
    >  def put(self, key, item):
        >  If the number of items in dict is higher than self.MAX_ITEMS:
            >  Must print DISCARD: with the key discarded, followed by new line
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ a caching system that uses a LIFO algorithm """

    def __init__(self):
        """ inherits methods and properties from parent """
        super().__init__()

    def put(self, key, item):
        """ add an item in the cache, discarding last item if items > MAX """
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
        return self.cache_data.get(key)
