# Define a dictionary named inventory to store item information.
inventory = {}

def add_item(item_id,name,quantity):
    item_details = {"name": name, "quantity": quantity}
    inventory[item_id] = item_details
    return inventory

add_item("A1","Shoes",5)

def check_stock(item_id):
    if item_id in inventory:
        item = inventory[item_id]
        print(f"Item: {item['name']}, Quantity: {item['quantity']}")
    else:
        print(f"Item with ID {item_id} not found in inventory.")

check_stock("A1")

def update_stock(item_id, delta):
    if item_id in inventory:
        inventory[item_id]["quantity"] += delta
        print(f"Stock for item {item_id} updated.")
    else:
        print(f"Item with ID {item_id} not found in inventory. Update failed.")

update_stock("A1",-2)