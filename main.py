

import random
from hangman_art import stages, logo
from hangman_word import eng_word, malay_word
from replit import clear

# welcome screen
print(logo)
print("Welcome to Hangman!")

while True:
  # choose lang
  lang = input("Please choose language (E for English/M for Malay): ").lower()
  
  if lang == "m":
    chosen_word = random.choice(malay_word)
    print("You have chosen Malay language!")
    break
  elif lang == "e":
    chosen_word = random.choice(eng_word)
    print("You have chosen English language!")
    break
  else:
    print("You have entered invalid choice!")


display=[]
hangman = 6
guessed_letter = []

# create display to guess
for _ in chosen_word:
  display.append("_")

while '_' in display:
  
  guess = input("Enter a letter to guess: ").lower() 
  clear()
  print(logo)
  
  # no guess
  if guess == "":
    continue

  # already guessed
  if guess in guessed_letter:
    print("You already guess the letter ", guess)
    print(stages[hangman])
    continue

  # add new letter to guessed letter list
  guessed_letter.append(guess)

  in_word = 0
  # if letter is in word
  for idx, letter in enumerate(chosen_word):
    if guess == letter:
      in_word = 1
      display[idx] = chosen_word[idx]

  print("Letter you have guessed: ", *guessed_letter, sep = " ")
  print(*display, sep = " ")

  # if guessed incorrectly
  if in_word==0:
    hangman -= 1
    print(stages[hangman])
    print(f"You guessed {guess} letter that is not in the word, you lose a life!")
    if hangman == 0:
      print("Game Over!")
      print("The solution is", chosen_word)
      break
  else:
    print(stages[hangman])
    print("You guessed correct!")
    
  # all letter guessed
  if '_' not in display:
    print("Congratulations! You won the game!")
    break

