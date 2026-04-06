#!/usr/bin/env python3
"""Module that takes a float n as argument"""

import math


def to_str(n: float) -> str | float:
    """Return a strings representation of the float """
    return math.floor(n)
