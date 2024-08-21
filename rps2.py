import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playAgain = True
while playAgain: 
    
    playerChoice = int(input("\nEnter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n"))


    if playerChoice < 1 or playerChoice > 3:
        sys.exit("You must enter 1, 2, or 3.")
        
    computerChoice = int(random.choice("123"))

    print("")
    print("You chose " + str(RPS(playerChoice)).lower().replace("rps.", "") + ".")
    print("Python chose " + str(RPS(computerChoice)).lower().replace("rps.", "") + ".")

    # if playerChoice == 1 and computerChoice == 3:
    #     print("You win!")
    # elif playerChoice == 2 and computerChoice == 1:
    #     print("You win!")
    # elif playerChoice == 3 and computerChoice == 2:
    #     print("You win!")
    if playerChoice == 1 and computerChoice == 3 or playerChoice == 2 and computerChoice == 1 or playerChoice == 3 and computerChoice == 2:
        print("🎉 You win!")
    elif playerChoice == computerChoice:
        print("😲 Game tied!")
    else:
        print("🐍 Python wins!")
    
    playAgain = input("\nPlay again? \nY for Yes or \nN for No \n")
    
    if playAgain.lower() == "y":
        continue
    else:
        print("\n🥳 Thank you for playing! \n")
        playAgain = False