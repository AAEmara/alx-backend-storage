#!/usr/bin/env python3
"""A module that defines a function that inserts a document."""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection.

    Args:
        mongo_collection (PyMongo Collection): A collection of documents.
        kwargs (dictionary): A dictionary that represents documents.

    Returns:
        The id of the newly created document.
    """
    new_document = dict()

    if kwargs is not None:
        for key, val in kwargs.items():
            new_document[key] = val

        result = mongo_collection.insert_one(new_document)
        return (result.inserted_id)
