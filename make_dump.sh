#!/bin/bash
# this script will be running after last parsed page from 'main.py' 

echo "Dumping postgresql data!"

pg_dump real_estate | gzip > dump.real_estate.gz

# for resore run
# gunzip dump.real_estate.gz
# psql db < dump


