#!/usr/bin/env python3

"""
Create a class called FIFOCache
that inherits from BaseCaching and is a caching system:
    >  Same as BasicCache except the following additions
    >  Can overload def __init__(self):
       but don't forget to call the parent init: super().__init__()
    >  def put(self, key, item):
        >  If the number of items in self.cache_data
           is higher than BaseCaching.MAX_ITEMS:
            >  Must discard the first item put in cache (FIFO algorithm)
            >  Must print DISCARD: with the key discarded, followed by new line
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ a caching system that uses a FIFO algorithm """

    def __init__(self):
        """ inherits methods and properties from parent """
        super().__init__()

    def put(self, key, item):
        """ add an item in the cache, discarding 1st item if items > MAX """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                disc_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(disc_key)
                print(f"DISCARD: {disc_key}")

    def get(self, key):
        """ get an item by key """
        return self.cache_data.get(key)
