#!/usr/bin/env python3
"""Module pagination"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return start and end index for pagination."""
    start = (page - 1) * page_size
    end = start + page_size

    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset.

        Returns:
            List[List]: The dataset of baby names, excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of data.

        Args:
            page (int): The page number (1-indexed). Defaults to 1.
            page_size (int): The number of rows per page. Defaults to 10.

        Returns:
            List[List]: A list of rows for the requested page,
            or empty list if page is out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.dataset()
        start, end = index_range(page, page_size)
        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return hypermedia pagination data.

        Args:
            page (int): The page number (1-indexed). Defaults to 1.
            page_size (int): The number of rows per page. Defaults to 10.

        Returns:
            dict: A dictionary containing pagination metadata with keys:
                - page_size (int): Number of items in the current page
                - page (int): Current page number
                - data (List[List]): The data for the current page
                - next_page (int or None): The next page number,
                or None if on last page
                - prev_page (int or None): The previous page number,
                or None if on first page
                - total_pages (int): Total number of pages
        """
        page_data = self.get_page(page, page_size)
        data = self.dataset()
        total_pages = math.ceil(len(data) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
