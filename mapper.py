#!/usr/bin/env python3

import sys
import json

# Function to safely split and parse concatenated JSON objects
def parse_concatenated_json(line):
    obj_start = 0
    depth = 0
    results = []
    in_string = False
    
    for i, char in enumerate(line):
        if char == '"' and (i == 0 or line[i - 1] != '\\'):
            in_string = not in_string
        elif not in_string:
            if char == '{':
                if depth == 0:
                    obj_start = i
                depth += 1
            elif char == '}':
                depth -= 1
                if depth == 0:
                    obj = line[obj_start:i + 1]
                    results.append(obj)
    
    return results

for line in sys.stdin:
    line = line.strip()
    
    # Get all JSON objects from the line
    json_objects = parse_concatenated_json(line)
    
    for obj in json_objects:
        try:
            data = json.loads(obj)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}", file=sys.stderr)
            continue

        city = data["city"]
        categories = data["categories"]
        sales_data = data.get("sales_data", {})

        total_revenue = 0
        total_cogs = 0
        has_valid_sales_data = False

        # Calculate the total revenue and COGS for top-selling categories
        for category in categories:
            if category in sales_data and "revenue" in sales_data[category] and "cogs" in sales_data[category]:
                total_revenue += sales_data[category]["revenue"]
                total_cogs += sales_data[category]["cogs"]
                has_valid_sales_data = True

        # Consider the store only if it has valid sales data for at least one top-selling category
        if has_valid_sales_data:
            net_return = total_revenue - total_cogs
            profit_or_loss = "profit_stores" if net_return > 0 else "loss_stores"

            # Emit the result
            output = {"city": city, profit_or_loss: 1}
            print(json.dumps(output))



