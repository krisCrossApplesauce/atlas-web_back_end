#!/usr/bin/env python3
"""
write a Python function that lists all documents in a collection
return an empty list if no document in the collection
"""
import pymongo

def list_all(mongo_collection):
    """ lists all docs in a collection """
    return [doc for doc in mongo_collection.find()]
