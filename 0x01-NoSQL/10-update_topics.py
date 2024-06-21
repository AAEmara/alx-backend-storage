#!/usr/bin/env python3
"""A module that defines a function that updates documents in PyMongo."""

from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]):
    """Updates the school's documents' topic according to a given name.

    Args:
        mongo_collection (PyMongo's Collection): A collection of schools.
        name: The name of the shcool to be updated.
        topics: The topics approached in the school.

    Returns:
        NOTHING
    """
    mongo_collection.update_one({"name": name},
                                {"$set": {"topics": topics}},
                                upsert=True)
