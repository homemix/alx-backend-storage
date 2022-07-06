#!/usr/bin/env python3
"""
generate and store values in redis
"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store the data in the cache
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) -> Union[str, bytes, int, float]:
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
        except Exception:
            value = 0
        return value
