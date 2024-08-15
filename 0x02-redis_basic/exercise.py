#!/usr/bin/env python3
"""A module that defines a class for the configuration of a Redis Client."""

import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(
            self,
            key: str, fn: Optional[Callable] = None
           ) -> Union[str, int, bytes, None]:
        """Converts the string bytes into the desired data type and returns it.
        Args:
            key: The key for the desired value.
            fn: The method to be used to convert the data type of the value.
        Returns:
            The converted value in the desired data type.
        """
        value: Union[bytes, None] = self._redis.get(key)  # Normal Redis GET.
        if (value is None or fn is None):
            return value  # The value is returned in bytes.
        converted_value = fn(value)  # Converting the value using a method.
        return (converted_value)  # Returning the converted value.

    def get_str(self, value: bytes) -> str:
        """Convert the string bytes into string data type and returns it.
        Args:
            value: The value for the desired value.
        Returns:
            The converted value as a string data type.
        """
        string_value = value.decode(encoding='utf-8', errors='strict')
        return string_value

    def get_int(self, value: bytes) -> int:
        """Convert the string bytes into integer data type and returns it.
        Args:
            value: The key for the desired value.
        Returns:
            The converted value as an integer data type.
        """
        integer_value = int(value)
        return integer_value
