#!/usr/bin/env python3
"""A module that provide stats about Nginx log stored in MongoDB."""


if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient()
    db = client.logs
    nginx = db.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_log = dict()

    logs_count = nginx.count_documents({})
    for method in methods:
        methods_log[method] = nginx.count_documents({"method": method})
    status_count = nginx.count_documents({"path": "/status"})

    print(f"{logs_count} logs")
    print("Methods:")
    for key, val in methods_log.items():
        print(f"\tmethod {key}: {val}")
    print(f"{status_count} status check")
