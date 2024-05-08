#!/usr/bin/env python3
"""Python Script"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """pagination func"""
    start_idx = (page * page_size) - page_size
    end_idx = page * page_size
    return (start_idx, end_idx)
