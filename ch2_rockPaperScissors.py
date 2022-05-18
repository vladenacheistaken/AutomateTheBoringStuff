"""Example output from the chapter that I will use to write a script without the author's solution:

ROCK, PAPER, SCISSORS
0 Wins, 0 Losses, 0 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
p
PAPER versus...
PAPER
It is a tie!
0 Wins, 1 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
s
SCISSORS versus...
PAPER
You win!
1 Wins, 1 Losses, 1 Ties
Enter your move: (r)ock (p)aper (s)cissors or (q)uit
q"""

import random
import time

noWins = 0  # initialize win, loss, tie counters
noLoss = 0
noTies = 0

print("ROCK, PAPER, SCISSORS")
print(str(noWins) + ", " + str(noLoss) + ", " + str(noTies))

print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
playerChoice = input()

while playerChoice != "q":
    while playerChoice.lower() != "r" or playerChoice.lower() != "p" or playerChoice.lower() != "s":
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")

    computerChoice = random.randint(1, 3)

    if playerChoice == "r" and computerChoice == 1:
