#!/usr/bin/env python3
"""
Module 9-insert_school
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: pymongo collection object
        **kwargs: fields of the document to insert

    Returns:
        The new document _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
