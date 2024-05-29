#!/usr/bin/python3
""" BasicCache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """fifo cashing"""

    def put(self, key, item):
        """puts an item"""
        if item and key:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_key)
                print(f'DISCARD: {first_key}')

    def get(self, key):
        """gets an item"""
        if key:
            return self.cache_data.get(key)
