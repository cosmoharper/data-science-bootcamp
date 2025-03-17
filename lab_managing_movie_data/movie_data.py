# Define the variables
movie_info = ("The Shawshank Redemption", "Frank Darabont")  # tuple for immutable data
cast = ["Tim Robbins", "Morgan Freeman", "Bob Gunton"]      # list for mutable data
new_actor = "William Sadler"

# Accessing Movie Data
print("Movie Title:", movie_info[0])        # Access title (first element of tuple)
print("Director:", movie_info[1])          # Access director (second element of tuple)
print("Lead Actor:", cast[0])              # Access first actor in cast list
print("Current Cast:", cast)               # Print full cast list

# Modifying Cast List - Adding new actor
cast.append(new_actor)                     # Add new actor to the end of the list
print("Updated Cast:", cast)               # Print updated cast list