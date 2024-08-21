import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
            
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(f"\nHello {name}!\nPlease Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n")    
        
        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()
            
        player = int(playerchoice)
        computerchoice = random.choice("123")
        computer = int(computerchoice)
        
        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")
        
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            
            if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you win!"
            elif player == computer:
                return "😲 Game tied!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}...😔"
        
        game_result = decide_winner(player, computer)
        print(game_result)
        nonlocal game_count
        game_count += 1
        print(f"\nGame count: {game_count}")
        print(f"\n{name}\'s wins: {player_wins}")
        print(f"\nPython\'s wins: {python_wins}")
        
        print(f"\nPlay again, {name}?")
        while True:
            playagain = input("\nY for Yes or \nN for No \n")
            if playagain.lower() not in ["y","n"]:
                continue
            else:
                break
        
        if playagain.lower() == "y":
            return play_rps()
        else:
            print(f"\n🥳 Thank you for playing, {name}! \n\nSee you next time!")
            playagain = False
            if __name__ == "__main__":
                sys.exit()
            else:
                return
            # sys.exit()
    return play_rps



if __name__ == "__main__":
    
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )
    

    args = parser.parse_args()
    
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()

 