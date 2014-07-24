#!/bin/bash

read -p "You're going to download the full weibo corpus from HKU (57 files, 18G).
Are you sure(y/n)?" choice

case "$choice" in 
# to download the data
  y|Y ) 
    wget -r "http://147.8.142.179/datazip/"
    #  Downloaded: 57 files, 18G in 6h 42m 3s (803 KB/s)
    
    echo "renaming DIR to data"    
    mv 147.8.142.179/datazip data/datazip ;;
    rm -R 147.8.142.179 ;;

    echo "now unziping files"
    ls data/datazip/*zip | xargs -i rm {}

  n|N ) echo "Ok, bye.";;
  * ) echo "invalid input";;
esac

