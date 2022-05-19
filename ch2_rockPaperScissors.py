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

import random, time

winCount = 0  # initialize win, loss, tie counters
lossCount = 0
tieCount = 0

print("ROCK, PAPER, SCISSORS")
print(str(winCount) + " Wins, " + str(lossCount) + " Losses, " + str(tieCount) + " Ties")

print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
playerChoice = input()

choiceDictionary = {"r": "ROCK",
                    "p": "PAPER",
                    "s": "SCISSORS",
                    "q": "QUIT"}  # dictionary of choices used in input validation & picking the computer move

while playerChoice not in choiceDictionary:
    print("Please enter (r)ock (p)aper (s)cissors or (q)uit")
    playerChoice = input()

    while playerChoice.lower() != choiceDictionary[3]:  # while user does not type "q"
        computerChoiceIndex = random.randint(0, 2)
        computerChoice = choiceList[computerChoiceIndex]

        if playerChoice == computerChoice:

            print("It is a tie!")

