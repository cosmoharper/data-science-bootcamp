
age = int(input("What is your age? "))
movie_type = input("What type of movie do you want to see (regular/premium)? ").lower

def ticket_price(age, movie_type):
    ticket_price = 0

    if age <= 12:
        if movie_type == "regular":    
            ticket_price = 8
        elif movie_type == "premium":
            ticket_price = 12
    elif age in range(13, 60):
        if movie_type == "regular":
            ticket_price = 12
        elif movie_type == "premium":
            ticket_price = 15
    else:
        if movie_type == "regular":
            ticket_price = 10
        elif movie_type == "premium":
            ticket_price = 12
    
    return ticket_price

result = ticket_price(age, movie_type)
print(f"The price of your ticket is ${result}")