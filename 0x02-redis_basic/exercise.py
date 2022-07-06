#!/usr/bin/env python3
"""
generate and store values in redis
"""
from functools import wraps

import redis
import uuid
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
        Counts the number of times a method is called.
   """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator to store the history of inputs and
    outputs for a particular function.
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):  # sourcery skip: avoid-builtin-shadow
        """ Wrapper for decorator functionality """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper


class Cache:
    """
    get the value from the cache
    """

    def __init__(self) -> None:
        """
        initialize the redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store the data in the cache
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        get the data from the cache
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        get the data from the cache
        """
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key: str) -> int:
        """
        get the data from the cache
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except:
            value = 0
        return value
