import sys
import random
from enum import Enum

def play_rps():
        
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("\nEnter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n")    
    
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()
        
    player = int(playerchoice)
    computerchoice = random.choice("123")
    computer = int(computerchoice)
    
    print("\nYou chose " + str(RPS(player)).lower().replace("rps.", "") + ".")
    print("Python chose " + str(RPS(computer)).lower().replace("rps.", "") + ".\n")

    if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😲 Game tied!")
    else:
        print("🐍 Python wins!")
    
    print("\nPlay again?")
    while True:
        playagain = input("\nY for Yes or \nN for No \n")
        if playagain.lower() not in ["y","n"]:
            continue
        else:
            break
    
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🥳 Thank you for playing! \n")
        playagain = False
        sys.exit("Bye!")
        
play_rps()