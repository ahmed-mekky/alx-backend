#!/usr/bin/python3
""" BasicCache module"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Basic Cache"""

    def put(self, key, item):
        """puts an item"""
        if item and key:
            self.cache_data[key] = item

    def get(self, key):
        """gets an item"""
        if key:
            return self.cache_data.get(key)
