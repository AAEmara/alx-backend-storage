#!/usr/bin/env python3
"""A module that defines a function that filters a collection."""


def schools_by_topic(mongo_collection, topic: str):
    """Filters a collection with a given topic.

    Args:
        mongo_collection (PyMongo's Collection): A collection of schools.
        topic: The document's key that we will use to filer the Collection.

    Returns:
        A list of schools PyMongo's Collection Objects.
    """
    return (mongo_collection.find({"topics": topic}))
