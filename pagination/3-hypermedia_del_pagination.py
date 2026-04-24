#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def init(self):
        self.dataset = None
        self.indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.dataset = dataset[1:]

        return self.dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.indexed_dataset is None:
            dataset = self.dataset()

            self.indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a deletion-resilient page and pagination metadata."""
        dataset = self.indexed_dataset()
        if index is None:
            index = 0

        assert type(index) is int and 0 <= index < len(self.dataset())
        assert type(page_size) is int and page_size > 0

        data = []
        next_index = index

        while len(data) < page_size and next_index < len(self.dataset()):
            if next_index in dataset:
                data.append(dataset[next_index])
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
