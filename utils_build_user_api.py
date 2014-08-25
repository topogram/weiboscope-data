#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
from lib.users import UserAPI

api=UserAPI()

#config stuff
if "TOPOGRAM_RAW_DATA_PATH" in os.environ:
    raw_path=os.environ.get('TOPOGRAM_RAW_DATA_PATH')
else: raise Exception("TOPOGRAM_RAW_DATA_PATH is not defined !")

userdata_file=os.path.join(raw_path, "userdata.csv")

print userdata_file
# number of lines : 14,388,386 users

with open(userdata_file, 'rb') as csvfile:
    i=0

    user_data=csv.reader(csvfile)
    csvfile.next() #skip csv header
    print "Storing users in MongDB... Please Wait."

    for row in user_data:
        api.create_user(row)
        i+=1
        
print "%d users saved"%i