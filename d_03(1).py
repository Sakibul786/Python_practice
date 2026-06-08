print("Welcome to the rollarcoaster ride!")
height = float(input("What is your height in cm?"))
if height >= 120:
    print("You can ride the rollarcoaster!")
    age = int(input("What is your age?"))
    if age <= 12:
        print("Please pay $6.")
    elif age <= 17:
        print("Please pay $8.")
    else:
        print("Please pay $12.")    
else:
    print("Sorry, you have to grow taller before you can ride.")
