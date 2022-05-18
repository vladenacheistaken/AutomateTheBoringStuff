"""Example output from the chapter that I will use to write a script without the author's solution:

I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
17
Your guess is too high.
Take a guess.
16
Good job! You guessed my number in 4 guesses!"""

import random
import time

nrToGuess = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
time.sleep(1)
print('Take a guess.')

userInput = input()

while not userInput.isnumeric():  # validate that the user enters only numbers
    print('Please enter a number.')
    userInput = input()

nrOfGuesses = 0  # initialize number of guesses

while int(userInput) != nrToGuess:
    if int(userInput) < nrToGuess:
        print("Your guess is too low.")
        userInput = input()
        nrOfGuesses += 1
    elif int(userInput) > nrToGuess:
        print("Your guess is too high.")
        userInput = input()
        nrOfGuesses += 1

print("Good job! You guessed my number in " + str(nrOfGuesses + 1) + " attempts!")  # +1 to account for the initial guess

"""Author's script:

# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + '
guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))"""
