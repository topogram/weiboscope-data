#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from pymongo.errors import ConnectionFailure
from pymongo import Connection


#config stuff
if "TOPOGRAM_MONGO_HOST" in os.environ:
    host=os.environ.get('TOPOGRAM_MONGO_HOST')
else: host="localhost"

if "TOPOGRAM_MONGO_PORT" in os.environ:
    port=os.environ.get('TOPOGRAM_MONGO_PORT')
else: port=27017

class MongoDB:

    def __init__(self, db):
        print 
        print """Connecting to MongoDB... """

        try:
            # connect to mongo
            self.connection = Connection(host=host, port=port)

            # connect to db
            self.db = self.connection[db]
            print "Connected successfully MongoDB at %s:%s" %(host, str(port))
            print 

        except ConnectionFailure, e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)
    
    def save_data(self, data, collection):
        # create /select collection
        weiboData = self.db[collection]
        weiboData.insert(data, safe=True)
        print "stored in Mongo, collection: "+collection