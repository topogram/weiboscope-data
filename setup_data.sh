#!/bin/bash

# to download the data
bash dl_raw_data.sh

#  Downloaded: 57 files, 18G in 6h 42m 3s (803 KB/s)

# move the files to the data folder
mv 147.8.142.179/datazip data/datazip
rm -R 147.8.142.179

# remove zip files
ls data/datazip/*zip | xargs -i rm {}

# create user API
