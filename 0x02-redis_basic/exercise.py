#!/usr/bin/env python3
"""
generate and store values in redis
"""
import redis
import uuid


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

    def store(self, data) -> str:
        """
        store the data in the cache
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
