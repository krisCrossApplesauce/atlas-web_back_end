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


if __name__ == "__main__":
    """ ok, not so weird of a traceback error, I understand it now,
    couldn't import my file bc of errors
    """
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    my_collection = client.logs.nginx

    print(f"{my_collection.count()} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(f"method {method}: {my_collection.count_documents({"method": method})}")
    print(f"{my_collection.count_documents({"method": "GET", "path": "/status"})} status check")
