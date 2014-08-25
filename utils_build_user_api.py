#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import csv
from lib.users import UserAPI

#config stuff
# if "TOPOGRAM_RAW_DATA_PATH" in os.environ:
#     raw_path=os.environ.get('TOPOGRAM_RAW_DATA_PATH')
# else: raise Exception("TOPOGRAM_RAW_DATA_PATH is not defined !")



def create_user_api(userdata_file):
    api=UserAPI()

    with open(userdata_file, 'rb') as csvfile:
        i=0
        user_data=csv.reader(csvfile)
        csvfile.next() #skip csv header
        print "Storing users in MongDB... Please Wait."

        for row in user_data:
            api.create_user(row)
            i+=1
            
    # number of lines : 14,388,386 users
    print "%d users saved"%i

if __name__ == "__main__":
    if os.path.isfile(sys.argv[1]) :
        # and sys.argv[1][0:len("userdata.csv")] == "userdata.csv":
        create_user_api(sys.argv[1])
    else :
        raise ValueError("File name should be userdata.csv")
