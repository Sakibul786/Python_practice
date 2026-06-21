import random

# Create a list
fruits = ["Apple", "Banana", "Orange"]

# Print the whole list
print("Original list:", fruits)

# Access elements using index
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Add a new item
fruits.append("Mango")
print("After append:", fruits)

# Remove an item
fruits.remove("Banana")
print("After remove:", fruits)

# Length of the list
print("Number of fruits:", len(fruits))

# Sort the list
fruits.sort()
print("Sorted list:", fruits)

# Reverse the list
fruits.reverse()
print("Reversed list:", fruits)

# Choose a random fruit
random_fruit = random.choice(fruits)
print("Random fruit:", random_fruit)

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print("Random number:", random_number)