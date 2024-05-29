#!/usr/bin/python3
""" BasicCache module"""
from base_caching import BaseCaching


class LIFOCache (BaseCaching):
    """lifo cashing"""

    def __init__(self):
        super().__init__()
        self.used_counter = {}

    def put(self, key, item):
        """puts an item"""
        if item and key:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                list_item = min(self.used_counter, key=self.used_counter.get)
                self.cache_data.pop(list_item)
                self.used_counter.pop(list_item)
                print(f'DISCARD: {list_item}')
            self.cache_data[key] = item
            self.used_counter[key] = 0

    def get(self, key):
        """gets an item"""
        if key:
            self.used_counter[key] += 1
            return self.cache_data.get(key)
