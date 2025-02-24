#!/bin/bash

# Base URL for the GitHub release
BASE_URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/"

# Array of files to download (2019 and 2020 data)
FILES=(
    "yellow_tripdata_2019-01.csv.gz"
    "yellow_tripdata_2019-02.csv.gz"
    "yellow_tripdata_2019-03.csv.gz"
    "yellow_tripdata_2019-04.csv.gz"
    "yellow_tripdata_2019-05.csv.gz"
    "yellow_tripdata_2019-06.csv.gz"
    "yellow_tripdata_2019-07.csv.gz"
    "yellow_tripdata_2019-08.csv.gz"
    "yellow_tripdata_2019-09.csv.gz"
    "yellow_tripdata_2019-10.csv.gz"
    "yellow_tripdata_2019-11.csv.gz"
    "yellow_tripdata_2019-12.csv.gz"
    "yellow_tripdata_2020-01.csv.gz"
    "yellow_tripdata_2020-02.csv.gz"
    "yellow_tripdata_2020-03.csv.gz"
    "yellow_tripdata_2020-04.csv.gz"
    "yellow_tripdata_2020-05.csv.gz"
    "yellow_tripdata_2020-06.csv.gz"
    "yellow_tripdata_2020-07.csv.gz"
    "yellow_tripdata_2020-08.csv.gz"
    "yellow_tripdata_2020-09.csv.gz"
    "yellow_tripdata_2020-10.csv.gz"
    "yellow_tripdata_2020-11.csv.gz"
    "yellow_tripdata_2020-12.csv.gz"
)

# Download each file
for FILE in "${FILES[@]}"; do
    wget "${BASE_URL}${FILE}"
    gunzip "${FILE}"
done

echo "All files downloaded."