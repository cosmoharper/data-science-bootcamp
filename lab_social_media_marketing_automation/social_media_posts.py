# Lab: Social Media Marketing Automation

products = [
    {"image": "product1.jpg", "description": "Introducing our new wireless headphones!"},
    {"image": "product2.png", "description": "The perfect summer sandals are here!"}
]

platforms = ["Facebook", "Twitter", "Instagram"]

def print_product_info():
    for product in products:
        image = product["image"]
        description = product["description"]
        print(f"Product Post: Image - {image}, Description - {description}")

def print_post_by_platform():
    for platform in platforms:
        for product in products:
            image = product["image"]
            description = product["description"]
            print(f"Platform: {platform} - Post: Image - {image}, Description - {description}")

# Call the functions to see the output
print_product_info()
print_post_by_platform()