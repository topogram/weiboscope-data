#!/bin/bash

export TOPOGRAM_MONGO_HOST='localhost'
export TOPOGRAM_MONGO_PORT=27017
export TOPOGRAM_MONGO_DB='weiboscope'
export TOPOGRAM_RAW_DATA_PATH=`pwd`
export TOPOGRAM_TMP_PATH="/tmp"
export TOPOGRAM_ES_HOST="http://localhost:9200"

# Download the data
bash dl_raw_data.sh

# Parse user data in Mongo
python utils_build_user_api.py

# Build provinces information
python utils_build_provinces_stats.py

# Index
python es_build_index.py

echo "Data processing done !"