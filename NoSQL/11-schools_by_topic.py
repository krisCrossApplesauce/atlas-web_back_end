#!/usr/bin/env python3
"""
write a Python func that returns the list of school having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ I'm pretty sure it should be basically
    the same as searching for something by the name attribute
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
