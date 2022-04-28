#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from replit import clear

def guess():
  return random.randint(1,100)

def level_of_difficulty(attempts):
  #attempts = 10
  computer_number = guess()
  loop = True
  while attempts > 0 and loop:
    print(f"You have {attempts} to guess the number")
    user_number = int(input("Make a guess: "))
    if user_number == computer_number:
      print(f"You got it! The answer was {computer_number}")
      loop = False
    elif user_number > computer_number:
      print("Too high")
      if attempts > 1:
        print("Guess again")
      attempts -=1
    else:
      print("Too low")
      if attempts > 1:
        print("Guess again")
      attempts-=1
  if attempts == 0:
    print("You've run out of guesses, You lose")


def number_guess():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  #computer_number = guess()
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    level_of_difficulty(10)
  else:
    level_of_difficulty(5)
  play_or_not = input("Do you want to play game again. Type 'y' to continue and 'n' to not: ")
  if play_or_not == 'y':
    clear()
    number_guess()

#computer_number = guess()
#print(computer_number)
number_guess()
