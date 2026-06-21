import random

# simple function
def greet():
    print("Hello! Welcome to Python")

greet()


# function with parameters
def add(a, b):
    print("Sum =", a + b)

add(5, 3)
add(10, 20)


# function with return value
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print("Multiplication =", result)


# function with if-else
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(check_age(20))
print(check_age(15))


# function with list
def show_fruits(fruits):
    for f in fruits:
        print("Fruit:", f)

my_fruits = ["apple", "banana", "mango"]

show_fruits(my_fruits)


# function with random
def random_choice(items):
    return random.choice(items)

colors = ["red", "green", "blue"]

print("Random color:", random_choice(colors))