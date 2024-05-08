#!/usr/bin/env python3
"""Python Script"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        if type(page) is not int or type(page_size) is not int or page * page_size <= 0:
            raise AssertionError

        assert page > 0 and page_size > 0
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            idxs = index_range(page, page_size)
            dataset = [row for row in reader]
            return dataset[idxs[0]:idxs[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """pagination func"""
    start_idx = (page * page_size) - page_size
    end_idx = page * page_size
    return (start_idx, end_idx)
