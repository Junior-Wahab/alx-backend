#!/usr/bin/env python3
# 0-simple_helper_function.py

""" Pagination Exercises """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing a start & end index
    corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
