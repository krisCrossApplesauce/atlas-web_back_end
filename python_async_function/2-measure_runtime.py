#!/usr/bin/env python3

"""
import wait_n from the prev file.
create a function called measure_time
that takes ints called n and max_delay as args
and measures the total execution time for wait_n(n, max_delay)
and returns a float that is total_time / n
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """ returns the average amount of time it takes to run wait_random """
    before = time.time()
    asyncio.run(wait_n(n, max_delay))
    after = time.time()
    total_time = after - before

    return total_time / n
