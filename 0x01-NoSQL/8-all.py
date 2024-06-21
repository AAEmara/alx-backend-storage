#!/usr/bin/env python3
"""A module that defines a function with PyMongo library."""


def list_all(mongo_collection):
    """Lists all of the documents in a given collection.

    Args:
        mongo_collection (PyMongo's Collection): A mongo collection.

    Returns:
        If the collection is empty:
            An empty list.
        Else:
            The PyMongo's Collection Object(s).
    """
    result = mongo_collection.find()
    if (not (result)):
        return (list())
    return (result)
