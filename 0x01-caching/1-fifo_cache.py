#!/usr/bin/python3
""" BasicCache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """fifo cashing"""

    def put(self, key, item):
        """puts an item"""
        if item and key:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.popitem(last=False)
            self.cache_data[key] = item

    def get(self, key):
        """gets an item"""
        if key:
            return self.cache_data.get(key)
