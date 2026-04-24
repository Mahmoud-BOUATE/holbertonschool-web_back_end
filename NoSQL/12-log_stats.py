#!/usr/bin/env python3
"""
Log stats script using MongoDB
"""

from pymongo import MongoClient


def log_stats():
    """Displays stats about Nginx logs"""
    client = MongoClient()
    collection = client.logs.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods count
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # GET /status count
    status_check = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
