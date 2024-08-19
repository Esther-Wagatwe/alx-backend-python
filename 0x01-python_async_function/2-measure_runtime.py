#!/usr/bin/env python3
"""Module to Measures the total execution time for wait_n(n, max_delay)"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function that  measures the total execution time
    Return: float: total_time / n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    return (end - start) / n
