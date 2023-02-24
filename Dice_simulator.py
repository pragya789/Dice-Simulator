import random
print("Welcome to the game:)")
start = input("Are you ready to start the game? ")
if start != "yes":
    exit()


while (True):
    print(random.randint(1, 6))
    another_roll = input("Want to roll the dice again?")
    if another_roll.lower() == "yes":
        continue
    else:
        break