#!/bin/bash

url="https://countrymeters.info/en/World"
html=$(curl -s "$url")
datetime=$(date +"%Y-%m-%d %H:%M:%S")

population_growth_today=$(echo "$html" | grep -Po '(?<=<td class="counter"><div id="cp13">)[^<]+')

echo "$population_growth_today" >> /home/arnaudchn/PROJET/data.csv
