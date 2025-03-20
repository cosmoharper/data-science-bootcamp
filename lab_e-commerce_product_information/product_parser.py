# Import scrapers (if needed)
import requests
from bs4 import BeautifulSoup

# Sample product listings
listings = [
    "Apple iPhone 13 (128GB) - $999",
    "Samsung Galaxy S22 Ultra, 256GB - Starting at $1188",
    "Google Pixel 6/Pro - 512GB @ $890"
]

# List to store results
results = []

# Process each listing
for listing in listings:
    product_info = {} # Dictionary to store product info
    
    
    if "-" in listing: # Handle hyphen delimiter
        name, price = listing.split("-")
    elif "@" in listing: # Handle @ delimiter
        name, price = listing.split("@")
    elif "," in listing: # Handle comma delimiter
        name, price = listing.split(",")
    else:
        name, price = listing, ""
  
    product_info["name"] = name.strip()

    # Find price position and extract price
    price_index = price.find("$") # Check if $ symbol is found
    if price_index != -1:
        price_str = price[price_index+1:].split()[0] # Get everything before price
        product_info["price"] = float(price_str) # Convert first number after $ to float
    else:
        product_info["price"] = None

    # Add product info to results
    results.append(product_info)

# Print results
print(results)
