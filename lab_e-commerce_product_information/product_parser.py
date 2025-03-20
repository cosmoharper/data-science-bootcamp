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
    # Dictionary to store product info
    product_info = {}

    # Find price position and extract price
    price_index = listing.find("$")
    if price_index != -1:  # Check if $ symbol is found
        price_str = listing[price_index+1:]
        price = float(price_str.split()[0])  # Convert first number after $ to float
        product_info["price"] = price

        # Extract name based on different delimiters
        name_part = listing[:price_index].strip()  # Get everything before price

        if "-" in name_part:
            # Handle hyphen delimiter
            name_split = name_part.split("-")
            product_info["name"] = name_split[0].strip()
            if len(name_split) > 1:
                product_info["details"] = name_split[1].strip()

        elif "," in name_part:
            # Handle comma delimiter
            name_split = name_part.split(",")
            product_info["name"] = name_split[0].strip()
            if len(name_split) > 1:
                product_info["details"] = name_split[1].strip()

        else:
            # Handle other formats (like @ delimiter)
            if "@" in name_part:
                name_split = name_part.split("@")
                product_info["name"] = name_split[0].strip()
                if len(name_split) > 1:
                    product_info["details"] = name_split[1].strip()
            else:
                product_info["name"] = name_part.strip()

        # Try to extract brand (simple approach: first word)
        brand = product_info["name"].split()[0]
        product_info["brand"] = brand

    # Add product info to results
    results.append(product_info)

# Print results
print("Parsed Product Listings:")
for i, product in enumerate(results, 1):
    print(f"\nProduct {i}:")
    for key, value in product.items():
        print(f"{key}: {value}")
