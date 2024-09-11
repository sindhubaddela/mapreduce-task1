#!/usr/bin/env python3
import sys
import json

# Dictionary to store the aggregated results for each city
city_stats = {}

for line in sys.stdin:
    # Parse the JSON object from the input line
    data = json.loads(line.strip())
    
    city = data["city"]
    
    # Initialize the city's entry in the dictionary if it doesn't exist
    if city not in city_stats:
        city_stats[city] = {"profit_stores": 0, "loss_stores": 0}
    
    # Increment the appropriate count (profit or loss) based on the data
    if "profit_stores" in data:
        city_stats[city]["profit_stores"] += data["profit_stores"]
    if "loss_stores" in data:
        city_stats[city]["loss_stores"] += data["loss_stores"]

# Output the aggregated results for each city
for city, counts in city_stats.items():
    result = {"city": city, "profit_stores": counts["profit_stores"], "loss_stores": counts["loss_stores"]}
    print(json.dumps(result))

