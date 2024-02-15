#!/usr/bin/env python3
"""
write a Python func that changes all topics of a school doc based on name:
name (string) will be the school name to update
topics (list of strings) will be the list of topics approached in the school
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """ changes topics of a school """
    mongo_collection.update_one(
        {'name': name},
        {"$set": {'topics': str(topics)}}
    )
