#!/usr/bin/python3
""" BasicCache module"""
from base_caching import BaseCaching


class LIFOCache (BaseCaching):
    """lifo cashing"""

    def put(self, key, item):
        """puts an item"""
        if item and key:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_item = self.cache_data.popitem()
                print(f'DISCARD: {last_item}')
            self.cache_data[key] = item

    def get(self, key):
        """gets an item"""
        if key:
            return self.cache_data.get(key)
