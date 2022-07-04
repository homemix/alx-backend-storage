#!/usr/bin/env python3
"""
MongoDB Operations with Python using pymongo insert
"""


def insert_school(mongo_collection, **kwargs):
    """ Insert a document into MongoDB """
    try:
        mongo_collection.insert_one(kwargs)
        return True
    except Exception as e:
        print(e)
        return False
