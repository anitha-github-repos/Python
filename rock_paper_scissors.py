rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

l = [rock,paper,scissors]
userinput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if userinput >2 or userinput<0:
  print("please enter a valid number")
computerinput = random.randint(0,(len(l)-1))
print(userinput)
print(l[userinput])
print("Computer chose\n",l[computerinput])

if userinput == 0 and computerinput == 2:
  print("you win!")
elif userinput == 1 and computerinput == 0:
  print("you win!")
elif userinput == 2 and computerinput == 1:
  print("you win!")
elif userinput == computerinput:
  print("It's a draw")
else:
  print("you lose")