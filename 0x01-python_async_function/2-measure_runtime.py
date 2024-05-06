#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) calls
    and returns the average time per call.

    Args:
        n (int): The number of calls to wait_n.
        max_delay (int): The maximum delay in seconds for each wait_n call.

    Returns:
        float: The average time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
