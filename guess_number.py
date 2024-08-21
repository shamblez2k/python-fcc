from random import choice
import sys

def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    
    def play_guess_number():
        nonlocal name
        nonlocal game_count
        nonlocal player_wins
        
        playerchoice = input(f"\nHi {name}! Guess which number I\'m thinking of? \nYour options are: 1,2 and 3.\n")
        
        if playerchoice not in["1","2","3"]:
            print(f"\n{name}, too bad! That wasn\'t even part of the options 💀")
            return play_guess_number()
        
        player = int(playerchoice)
        computerchoice = choice("123")
        computer = int(computerchoice)
        
        print(f"\n{name}, you chose {playerchoice}.")
        print(f"I was thinking about the number {computerchoice}")
        
        def decide_winner(player, computer):
            nonlocal player_wins
            if player == computer:
                player_wins += 1
                return f"🎉 You win, {name}!"
            else:
                return f"😔 Sorry, {name}. Better luck next time!"
        
        print(decide_winner(player, computer))
        game_count += 1
        print(f"\nGame count: {game_count}")
        print(f"{name}\'s wins: {player_wins}")
        print(f"Your winning percentage: {player_wins/game_count:.2%}")
        
        print(f"\nPlay again, {name}?")
        while True:
            playagain = input("\nY for Yes or \nN for No \n")
            if playagain.lower() not in ["y","n"]:
                continue
            else:
                break
        
        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print(f"\n🥳 Thank you for playing, {name}! \nSee you next time!")
            playagain = False
            if __name__ == "__main__":
                sys.exit()
            else:
                return
            # sys.exit("")
            
    return play_guess_number
            
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
    
    game_instance = guess_number(args.name)
    game_instance()

            
        
