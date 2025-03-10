# Main functionalities and inputs/outputs of the PizzaCost system:
# 1. Prompt the user for inputs:
#    • Pizza size (small or large)
#    • Number of toppings
#    • Delivery distance in miles
# 2. Calculate the base cost of the pizza using conditional statements.
# 3. Calculate the cost of toppings.
# 4. Calculate the delivery fee.
# 5. Sum up the total cost.
# 6. Display the result using an f-string.

'''
# Data Structure for PizzaCost system:
    user_phone = Integer
    pizza_quantity = Integer
    pizza_size = String
    toppings_quantity = Integer
    delivery_distance = Float
    base_cost = Float
    toppings_cost = Float
    delivery_cost = Float
    total_cost = Float
'''

# Pizza Shop Inputs
    small_pizza = 8
    large_pizza = 12
    toppings = 1
    delivery_fee_base = 2
    delivery_fee_extra = 1 * ({delivery_distance} - 5)

# 1. User inputs for User's Pizza Order
FUNCTION PizzaOrder
    user_phone = int(input("What is the phone number for this pizza order?"))
    pizza_quantity = int(input("How many pizzas would you like to order?"))
    pizza_size = input("What size pizza do you want to order (small/large)?")
    toppings_quantity = int(input("How many toppings do you want on the pizza(s)?)")
    delivery_distance = int(input("How many miles away is the destination of this order?)")
END FUNCTION

# 2. Calculate base cost of the order
FUNCTION BaseCost
    IF pizza_size == small:
        base_cost = pizza_quantity * small_pizza
    ELSE: 
        base_cost = pizza_quantity * large_pizza
    END IF
END FUNCTION

# 3. Calculate the cost of additional toppings
FUNCTION ToppingsCost
    IF toppings_quantity == 1:
        toppings_cost = 0
    ELSE:
        toppings_cost = toppings * toppings_quantity - 1
    END IF
END FUNCTION

# 4. Calculate the delivery fee
FUNCTION DeliveryCost
    IF delivery_distance is <= 5:
        delivery_cost = delivery_fee_base
    ELSE:
        delivery_cost = delivery_fee_base + delivery_fee_extra
    END IF
END FUNCTION

# 5. Sum up the total cost
FUNCTION TotalCost
    total_cost = base_cost + toppings_cost + delivery_cost
END FUNCTION