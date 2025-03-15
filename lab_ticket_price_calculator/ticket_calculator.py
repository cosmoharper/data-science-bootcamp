age = int(input("What is your age? "))
movie_type = input("What type of movie do you want to see (regular/premium)? ")

def ticket_price(age, movie_type):
    if age <= 12:
        return 8 if movie_type == "regular" else 10
    elif age in range(13, 60):
        return 12 if movie_type == "regular" else 15
    else:  # age > 60
        return 10 if movie_type == "regular" else 12

result = ticket_price(age, movie_type)
print(f"The price of your ticket is ${result}")
