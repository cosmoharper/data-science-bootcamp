import random

# Generate secret number
secret_number = random.randint(1,10)

# Initialize attempts
attempt_number = 0
allowed_attempts = 5
guess = 0

while attempt_number <= allowed_attempts and guess != secret_number:
    # Ask user for their guess
    guess = int(input("I am thinking of a number between 1 and 10. You have 5 guesses to get it right. What's your guess (1-10)? "))
    attempt_number += 1
    
    # If guess is less than the secret number, let them know and prompt to guess again.
    if guess < secret_number:
        print (f"Good guess, but your guess is less than the correct number. That's {attempt_number} of {allowed_attempts}. Guess again!")
    
    # If guess is more than the secret number, let them know and prompt to guess again.
    elif guess > secret_number:
        print(f"Good guess, but your guess is more than the correct number. That's {attempt_number} of {allowed_attempts}. Guess again!")
    
    # Give user feedback on guess relative to correct number
    else:
        print("That's correct! Great guess.") 
        break

if attempt_number > allowed_attempts:
    print(f"Good guessing, but the right answer was {secret_number}! Better luck next time.")