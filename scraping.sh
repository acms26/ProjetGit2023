#!/bin/bash
curl -s https://flightaware.com/live/airport/LFPO | grep -oP '<span class="flightRow.*?">\K.*?(?=</span>)' | awk '{printf "%s%s\n", $0, (NR%6==0 ? "\n" : "\t")}'

