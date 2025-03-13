# 1. User inputs for User's Pizza Order
user_phone = int(input("What is the phone number for this pizza order? "))
pizza_quantity = int(input("How many pizzas would you like to order? "))
pizza_size = input("What size pizza do you want to order (small/large)? ").lower()
toppings_quantity = int(input("How many toppings do you want on the pizza(s)? "))
delivery_distance = int(input("How many miles away is the destination of this order? "))

# Pizza Shop Inputs
small_pizza = 8
large_pizza = 12
toppings = 1
delivery_fee_base = 2
# Handle delivery fee extra (no extra fee if distance <= 5 miles)
delivery_fee_extra = 0 if delivery_distance <= 5 else 1 * (delivery_distance - 5)

# 2. Calculate base cost of the order
def BaseCost(pizza_size, pizza_quantity):
    base_cost = 0
    if pizza_size == "small":
        base_cost = pizza_quantity * small_pizza
    else: 
        base_cost = pizza_quantity * large_pizza
    return base_cost

# 3. Calculate the cost of additional toppings
def ToppingsCost(toppings, toppings_quantity):
    toppings_cost = 0
    if toppings_quantity <= 1:  
        toppings_cost = 0
    else:
        toppings_cost = toppings * (toppings_quantity - 1)
    return toppings_cost

# 4. Calculate the delivery fee
def DeliveryCost(delivery_fee_base, delivery_fee_extra):
    delivery_cost = delivery_fee_base + delivery_fee_extra  
    return delivery_cost

# Calculate all costs
base_cost = BaseCost(pizza_size, pizza_quantity)
toppings_cost = ToppingsCost(toppings, toppings_quantity)
delivery_cost = DeliveryCost(delivery_fee_base, delivery_fee_extra)

# 5. Sum up the total cost
def TotalCost(base_cost, toppings_cost, delivery_cost):
    total_cost = base_cost + toppings_cost + delivery_cost
    return total_cost

# Calculate and display results
total_cost = TotalCost(base_cost, toppings_cost, delivery_cost)

# Print the results
print(f"The base cost is ${base_cost}")
print(f"The toppings cost is ${toppings_cost}")
print(f"The delivery cost is ${delivery_cost}")
print(f"The total cost is ${total_cost}")