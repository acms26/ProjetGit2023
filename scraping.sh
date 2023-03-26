#!/bin/bash

url="https://countrymeters.info/en/World"
html=$(curl -s "$url")
datetime=$(date +"%Y-%m-%d %H:%M:%S")

world_population=$(echo "$html" | grep -Po '(?<=<td class="counter"><div id="cp1">)[^<]+')
population_growth_year_to_date=$(echo "$html" | grep -Po '(?<=<td class="counter"><div id="cp12">)[^<]+')

echo "$datetime;$world_population;$population_growth_year_to_date" >> /home/arnaudchn/PROJET/data.csv
