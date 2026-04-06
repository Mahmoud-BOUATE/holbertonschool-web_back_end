#!/usr/bin/env python3

"""Module that takes a list od int and floats and return their sum"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Sum of integers and floats"""
    return sum(mxd_list)
