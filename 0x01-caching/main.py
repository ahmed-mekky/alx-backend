#!/usr/bin/python3
"""
Test
"""
import sys

try:
    MRUCache = __import__('4-mru_cache').MRUCache

    my_cache = MRUCache()
    my_cache.print_cache()
    my_cache.put("test1", "myValue")
    my_cache.print_cache()
except:
    print(sys.exc_info()[1])
