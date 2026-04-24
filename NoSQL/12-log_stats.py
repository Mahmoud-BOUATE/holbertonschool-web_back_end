#!/usr/bin/env python3
"""
Nginx logs stats
"""

from pymongo import MongoClient


def count_docs(collection, filt):
    """Count documents with compatibility for older PyMongo versions."""
    try:
        return collection.count_documents(filt)
    except AttributeError:
        return collection.count(filt)


def print_nginx_stats():
    """Print required stats about Nginx logs."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    total_logs = count_docs(collection, {})
    print(f"{total_logs} logs")

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = count_docs(collection, {"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = count_docs(collection, {"method": "GET", "path": "/status"})
    print(f"\tmethod GET: {status_check} path /status")


if __name__ == "__main__":
    print_nginx_stats()
