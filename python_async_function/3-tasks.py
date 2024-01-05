#!/usr/bin/env python3

"""
import wait_random from 0-basic_async_syntax.
write a (regular, non-async) func called task_wait_random
that takes an int called max_delay
and returns a asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ returns an asyncio.Task """
    return asyncio.Task(wait_random(max_delay))
