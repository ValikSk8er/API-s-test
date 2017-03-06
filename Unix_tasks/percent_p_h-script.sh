#!/bin/bash
total_count=$(grep -c " 200 " datamining.log)
for hour in {00..23}; do grep '2014:'$hour datamining.log | echo "Percent successful requests per "$hour" hour =" $((($(grep -c "HTTP/1.1\" 200 ")*100)/$total_count))" %"; done > percent_per_hours.txt