#!/usr/bin/env python3
"""A module that defines a class for the configuration of a Redis Client."""

import redis
import uuid
from typing import Union


class Cache:
    """Configures a Redis Client.
    """
    def __init__(self):
        """Initializes the Cache Class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes some data and generates a key(uuid): value(data) pair.

        Args:
            data: The data that would be the value corresponding to the key.
        Returns:
            The random uuid key generated.
        """
        random_key = uuid.uuid4()
        self._redis.set(str(random_key), data)

        return (str(random_key))
