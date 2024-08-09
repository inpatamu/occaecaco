# Sample JSON object
top_holdings = {
    "Top_Holdings": [
        {"name": "ABC Corp", "weight": 10},
        {"name": "XYZ Corp", "weight": 8},
        {"name": "123 Corp", "weight": 6},
        # ... (additional holdings)
    ]
}

# Extract the top 10 holdings
top_10_holdings = top_holdings["Top_Holdings"][:10]

# Flatten the list of JSON objects into a single list
flattened_list = []
for holding in top_10_holdings:
    flattened_list.append({"name": holding["name"], "weight": holding["weight"]})

# Print the flattened list
print(flattened_list)
