#!/usr/bin/env python3
'''Task 3's module.
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that waits for a random
    delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: A task that waits for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
