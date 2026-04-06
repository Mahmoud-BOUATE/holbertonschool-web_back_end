#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""

from typing import Tuple


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """Function that calculate """
    return (k, v * v)
