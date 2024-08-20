import sys
import random

print("")

playerChoice = int(input("Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n"))


if playerChoice < 1 or playerChoice > 3:
    sys.exit("You must enter 1, 2, or 3.")
    
computerChoice = int(random.choice("123"))

print("")
print("You chose " + str(playerChoice) + ".")
print("Python chose " + str(computerChoice) + ".")

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