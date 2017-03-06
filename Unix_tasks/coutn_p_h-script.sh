#!/bin/bash
for hour in {00..23}; do grep '2014:'$hour datamining.log | echo 'Successful requests per hour '$hour' = '$(grep -c "HTTP/1.1\" 200 "); done > count_per_hours.txt