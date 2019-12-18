#MatchAnalysis.py
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates some kind of competitive game between two players A and B")
    print("The program requires A and B ability values (represented by decimals between 0 and 1)")

def getInputs():
    a = eval(input("Please enter player A's ability value (0-1):"))
    b = eval(input("Please enter player B's ability value (0-1):"))
    n = eval(input("Matches of the simulation game:"))
    return a, b, n

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("Competitive analysis begins, simulating {} games in total".format(n))
    print("Player A won {} matches, proportion {:0.1%}".format(winsA, winsA/n))
    print("Player B won {} matches, proportion {:0.1%}".format(winsB, winsB/n))

def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i  in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    return a == 15 or b == 15

main()
