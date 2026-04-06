#!/usr/bin/env python3
"""Module that creates an asyncio Task from a coroutine."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio Task for wait_random coroutine."""
    return asyncio.create_task(wait_random(max_delay))
