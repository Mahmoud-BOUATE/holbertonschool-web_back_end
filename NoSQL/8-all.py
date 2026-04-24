#!/usr/bin/env python3
"""List all document"""


def list_all(mongo_collection):
    """List all document"""
    return list(mongo_collection.find())
