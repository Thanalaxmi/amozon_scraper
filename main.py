import requests
import os
import json
SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")

params = {
    "api_key": SERPAPI_KEY,
    "engine": "amazon",
    "k":  "mac mini m4",
}

search = requests.get("https://serpapi.com/search", params=params)
response = search.json()

import csv

with open("amazon_results.csv", "w", newline='', encoding='utf-8') as csvfile:
    fieldnames = ["title", "asin", "thumbnail", "price", "rating", "reviews"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in response.get("organic_results", []):
        writer.writerow({
            "title": result.get("title"),
            "asin": result.get("asin"),
            "thumbnail": result.get("thumbnail"),
            "price": result.get("price"),
            "rating": result.get("rating"),
            "reviews": result.get("reviews")
        })
print("Data written to amazon_results.csv successfully.")