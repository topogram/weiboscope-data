#!/bin/bash

source ENV.sh

# Download the data
bash dl_raw_data.sh

# Parse user data in Mongo
python utils_build_user_api.py

# Build provinces information
python utils_build_provinces_stats.py

# Index
python es_build_index.py

echo "Data processing done !"
