# FOR LOOP + RANGE

print("FOR LOOP EXAMPLES")

# range(start, end) -> end is not included
for i in range(1, 6):
    print("Number:", i)  # prints 1 to 5

print("\nLoop with list")


# FOR LOOP WITH LIST

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print("Fruit:", fruit)  # prints each item in list

print("\nBREAK & CONTINUE")


# BREAK EXAMPLE

for i in range(1, 10):
    if i == 5:
        break  # loop stops when i = 5
    print("Break loop:", i)

print("\nCONTINUE EXAMPLE")


# CONTINUE EXAMPLE

for i in range(1, 6):
    if i == 3:
        continue  # skip number 3
    print("Continue loop:", i)

print("\nWHILE LOOP")


# WHILE LOOP

i = 1

while i <= 5:
    print("While loop:", i)
    i = i + 1  # increase value, otherwise infinite loop

print("\nWHILE LOOP WITH BREAK")


# WHILE LOOP WITH BREAK

j = 1

while True:  # infinite loop
    print("Infinite loop control:", j)
    j = j + 1

    if j == 4:
        break  # stop loop when j = 4