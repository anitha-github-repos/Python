import random
from replit import clear
from game_data import data
from art import logo,vs
# from itertools import permutations

def rand(compare,a):
  r = random.choice(data)
  print(f"{compare} {a}: {r['name']}, a {r['description']}, from {r['country']}")
  
  

r1 = random.choice(data)
r2 = random.choice(data)
while r1==r2:
  r2 = random.choice(data)
iteration = True
score = 0
i=0
print(logo)
while iteration:
  
  #rand("Compare","A")
  print(f"Compare A: {r1['name']}, a {r1['description']}, from {r1['country']}")
  print(vs)
  print(f"Againt B: {r2['name']}, a {r2['description']}, from {r2['country']}")
  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  i=i+1
  if user_choice == 'A':
    if r1['follower_count'] > r2['follower_count']:
      score +=1
      clear()
      print(logo)
      print(f"You're right! Current score: {score}")
    else:
      iteration = False
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
  else:
    if r1['follower_count'] < r2['follower_count']:
      score+=1
      clear()
      print(logo)
      print(f"You're right! Current score: {score}")
    else:
      iteration = False
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
  
  r1 = r2
  r2 = random.choice(data)
  while r1==r2:
    r2 = random.choice(data)
  

  


