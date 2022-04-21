import hangman_art
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
final_word = "_"*len(chosen_word)
#print(final_word)
l = list(chosen_word)
l2 = list(final_word)
#print(l2)
lives = 6
print(hangman_art.logo)
while "_" in l2 and lives:
  guess = input("Guess a letter: ").lower()
  for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
      l2[position] = guess
      #print("".join(l2))
  if guess not in chosen_word:
    lives-=1
    print("Entered letter not in the word, you lose a life ")
    print(hangman_art.stages[lives])
  if "".join(l2) == chosen_word:
    print("You Won")
  elif lives ==0:
    print("You loss")
  print("".join(l2))