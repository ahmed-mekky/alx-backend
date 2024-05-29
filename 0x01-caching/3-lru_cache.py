#!/usr/bin/python3
"""LRUCache module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """lru cashing"""

    def __init__(self):
        super().__init__()
        self.used_list = []

    def put(self, key, item):
        """puts an item"""
        if item and key:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                not key in self.cache_data.keys()):
                list_item = self.used_list.pop(0)
                self.cache_data.pop(list_item)
                print(f'DISCARD: {list_item}')
            self.cache_data[key] = item
            if key in self.used_list:
                self.used_list.remove(key)
            self.used_list.append(key)


    def get(self, key):
        """gets an item"""
        if key in self.cache_data.keys():
            self.used_list.remove(key)
            self.used_list.append(key)
            return self.cache_data.get(key)
