#!/usr/bin/env python3
"""
write a Python script that
provides some stats about Nginx logs stored in MongoDB:
   >  Database: logs
   >  Collection: nginx
   >  Display (same as the example):
       >  first line: x logs where x is the number of docs in the collection
       >  second line: Methods:
       >  five lines with the number of docs with the
          method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
       >  one line with the number of docs with:
           >  method=GET
           >  path=/status
"""
import pymongo


def log_stats_func(my_collection):
    """ come on, just work for me
    I wanna play Deep Rock Galactic with my friends :(
    """
    print(f"{my_collection.count()} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"method {method}: {my_collection.count({"method": [method]})}")
    print(f"{my_collection.count({
        "method": "GET",
        "path": "/status"
        })} status check")


if __name__ == "__main__":
    """ kinda a weird traceback error for the
    everything is documented checker but ok
    """
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    my_collection = client.logs.nginx

    log_stats_func(my_collection)
