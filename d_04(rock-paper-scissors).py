import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]
names = ["rock", "paper", "scissors"]

print("Rock Paper Scissors Game")
print("Choose: rock / paper / scissors")

user_input = input("Your choice: ").lower()

if user_input not in names:
    print("Invalid input")
else:
    user_index = names.index(user_input)
    user_choice = options[user_index]

    computer_index = random.randint(0, 2)
    computer_choice = options[computer_index]

    print("\nYour choice:")
    print(user_choice)

    print("Computer choice:")
    print(computer_choice)

    if user_index == computer_index:
        print("Result: Tie")

    elif (user_index == 0 and computer_index == 2) or \
         (user_index == 1 and computer_index == 0) or \
         (user_index == 2 and computer_index == 1):
        print("Result: You Win")

    else:
        print("Result: You Lose")