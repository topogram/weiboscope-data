#!/usr/bin/env python
# -*- coding: utf-8 -*-

from minimongo import Model, Index, configure
import os,json

# config
if "TOPOGRAM_MONGO_HOST" in os.environ:
    host=os.environ.get('TOPOGRAM_MONGO_HOST')
else: host="localhost"

if "TOPOGRAM_MONGO_PORT" in os.environ:
    port=os.environ.get('TOPOGRAM_MONGO_PORT')
else: port=27017

if "TOPOGRAM_MONGO_DB" in os.environ:
    db_name=os.environ.get('TOPOGRAM_MONGO_DB')
else: db_name="weiboscope"

# Mongo db
configure(host=host, port=port)

class User(Model):

    class Meta:
        # Here, we specify the database and collection names.
        # A connection to your DB is automatically created.
        database = db_name
        collection = "users"

        # Now, we programatically declare what indices we want.
        # The arguments to the Index constructor are identical to
        # the args to pymongo"s ensure_index function.
        # TODO : add indexes 
        indices = (
            Index("uid"),
            Index("province")
        )

        def __init__(self):
            pass