#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string and square of the numeric value."""
    return (k, v * v)
