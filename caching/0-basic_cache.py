#!/usr/bin/env python3

"""
Create a class called BasicCache
that inherits from BaseCaching and is a caching system:
    >  Must use self.cache_data - dict from the parent class BaseCaching
    >  This caching system doesn't have a limit
    >  def put(self, key, item):
        >  Must assign to self.cache_data the item value for the key key
        >  If key or item is None, this method should not do anything
    >  def get(self, key):
        >  Must return the value in self.cache_data linked to key
        >  If key is None or if the key doesn't exist in the dict, return None
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ a basic caching system """
    MAX_ITEMS = None

    def __init__(self):
        """ inherit methods and properties from parent """
        super().__init__()

    def put(self, key, item):
        """ add an item in the cache """
        if key != None and item != None:
            self.cache_data[key] = item

    def get(self, key):
        """ get an item by key """
        return self.cache_data.get(key)
