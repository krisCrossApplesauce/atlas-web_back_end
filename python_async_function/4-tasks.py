#!/usr/bin/env python3

"""
take the code from wait_n and alter it into a new func called task_wait_n.
the code is nearly identical to wait_n except task_wait_random is being called
"""
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """ runs task_wait_random n times and returns a list of the results """
    lst = []
    i = 0
    d = 0

    while i < n:
        d = await task_wait_random(max_delay)
        lst.append(d)
        i += 1

    return sorted(lst)
