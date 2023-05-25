#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)
chosen = False
lifes = 0
while not chosen:
    level=int(input("Choose difficulty level: 1. easy - 10 guesses, 2. hard - 5 guesses"))
    if level == 1:
        print("You chose easy level, and have 10 guesses in total")
        chosen = True
        lifes = 10
    elif level == 2:
        print("You chose hard level, and have 5 guesses in total")
        chosen = True
        lifes = 5
    else:
        print("Please choose 1 or 2")

number = random.randint(1,101)
print(f"{number}")
#guess=int(input("guess number between 1 to 100: "))
won = False
while lifes > 0 and not won:
    guess=int(input("guess number between 1 to 100: "))
    if number > guess:
        lifes-=1
        print(f"Too low,    {lifes} lifes remain.")
    elif number < guess:
        lifes-=1
        print(f"Too high,    {lifes} lifes remain.")
    elif number == guess:
        print(f"You won.")
        won=True
    if lifes == 0:
        print(f"You lost, Out of lifes")
        won = False


