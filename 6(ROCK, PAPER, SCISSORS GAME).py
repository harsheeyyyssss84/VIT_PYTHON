import random
import sys
items=["rock", "paper", "scissor", "scissors"]

computer=random.choice(items)

user=input("Select ROCK, PAPER, or SCISSOR: ").lower()

if user not in items:
    print("INVALID INPUT")
    sys.exit()


print("COMPUTER CHOOSES: ", computer)


if user == computer:
    print("MATCH DRAWWW!!!")

elif user == "rock" and computer == "scissor":
    print("USER WINSSS!!!")

elif user == "scissor" and computer == "paper":
    print("USER WINSSS!!!")

elif user == "paper" and computer == "rock":
    print("USER WINSSS!!!")

else:
    print("COMPUTER WINSSS!!!")