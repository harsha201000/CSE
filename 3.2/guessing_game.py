import random

# a random number to be guessed
answer = random.randint(1,50)

#  function that checks a guess
def check_guess(guess):
  guess = int(guess)
  if (guess < answer):
    print("You guessed too low")
    return False
  elif (guess > answer):
    print("You guessed too high")
  else:
    print("You guessed right!")
    
# the input prompts to begin the game
guess = input("You have three tries. Guess a number from 1 to 50: ")
check_guess(guess)

guess = input("Guess again: ")
check_guess(guess)

guess = input("Guess again: ")
check_guess(guess)

print("Did you win?")