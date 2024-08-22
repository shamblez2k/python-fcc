import sys
import random
from enum import Enum

# This is the first iteration of the tic-tac-toe game that I tried to code. It doesn't work properly and I haven't figured out what's wrong with it yet. I'll debug and figure it out later.

def tictactoe(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    python_wins = 0
    turn = ""
    player_symbol = "o"
    python_symbol = "x"
    
    # def decide_turn():
    #     nonlocal name
    #     nonlocal turn
    #     nonlocal player_symbol
    #     nonlocal python_symbol
    #     player = int(input(f"Hi {name}!\nPick 1 for heads or 2 for tails.\n"))
    #     if player == 1:
    #         print("You picked heads!")
    #     else:
    #         print("You picked tails!")
    #     decision = int(random.choice("12"))
    #     if decision == 1:
    #         print("Heads goes first!")
    #     else:
    #         print("Tails goes first!")
    #     if player == decision:
    #         print(f"🥳 Congratulations {name}! You'll go first, so you are x!\n")
    #         turn = "player"
    #         player_symbol = "x"
    #         python_symbol = "o"
    #     else:
    #         print("Python goes first, it is x!\n")
    #         turn = "python"
        # return decide_turn
            
    # coin_flip = decide_turn()
    # coin_flip()
    
    # decide_turn()
    
    decision_tree = [0,0,0,0,0,0,0,0,0]
    player_tree = [0,0,0,0,0,0,0,0,0]
    python_tree = [0,0,0,0,0,0,0,0,0]
    
    game_board = ["    |","   ","|    ","    |","   ","|    ","    |","   ","|    "]
    
    def play_game():
        nonlocal decision_tree
        nonlocal game_board
        nonlocal turn
        nonlocal name
        nonlocal game_count
        
        print(f"{game_board[0]}{game_board[1]}{game_board[2]}\n=============\n{game_board[3]}{game_board[4]}{game_board[5]}\n=============\n{game_board[6]}{game_board[7]}{game_board[8]}")
        
        if turn == "player":        
            playerchoice = input(f"\n😁 Hello {name}!\nLet\'s play a game of tic-tac-toe. Please Enter a number corresponding to the empty spaces available, as shown below: \n1 for top-left, \n2 for top-middle,\n3 for top-right,\n4 for middle-left, \n5 for middle-middle,\n6 for middle-right,\n7 for bottom-left, \n8 for bottom-middle,\n9 for middle-right: \n\n")    
        
            if playerchoice not in ["1", "2", "3","4","5","6","7","8","9"] or decision_tree[int(playerchoice)-1] !=0:
                print(f"Sorry, {name}, you must enter a valid choice.\nPlease enter a number between 1 and 9, based on the key given earlier.")
                return play_game()
        
            player = int(playerchoice)
            
            nonlocal player_symbol
            nonlocal player_tree
            #Update game-board
            if player == 1:
                game_board[0] = f"  {player_symbol} |"
                decision_tree[0] = 1
                player_tree[0] = 1
            elif player == 2:
                game_board[1] = f" {player_symbol} "
                decision_tree[1] = 1
                player_tree[1] = 1
            elif player == 3:
                game_board[2] = f"| {player_symbol}  "
                decision_tree[2] = 1
                player_tree[2] = 1
            elif player == 4:
                game_board[3] = f"  {player_symbol} |"
                decision_tree[3] = 1
                player_tree[3] = 1
            elif player == 5:
                game_board[4] = f" {player_symbol} "
                decision_tree[4] = 1
                player_tree[4] = 1
            elif player == 6:
                game_board[5] = f"| {player_symbol}  "
                decision_tree[5] = 1
                player_tree[5] = 1
            elif player == 7:
                game_board[6] = f"  {player_symbol} |"
                decision_tree[6] = 1
                player_tree[6] = 1
            elif player == 8:
                game_board[7] = f" {player_symbol} "
                decision_tree[7] = 1
                player_tree[7] = 1
            else:
                game_board[8] = f"| {player_symbol}  "
                decision_tree[8] = 1
                player_tree[8] = 1
            
            turn == "python"
        else:
            computerchoice = int(random.choice("123456789"))
            while decision_tree[computerchoice-1] !=0:
                computerchoice = int(random.choice("123456789"))
            
            python = computerchoice
            
            if python == 1:
                game_board[0] = f"  {python_symbol} |"
                decision_tree[0] = 1
                python_tree[0] = 1
            elif python == 2:
                game_board[1] = f" {python_symbol} "
                decision_tree[1] = 1
                python_tree[1] = 1
            elif python == 3:
                game_board[2] = f"| {python_symbol}  "
                decision_tree[2] = 1
                python_tree[2] = 1
            elif python == 4:
                game_board[3] = f"  {python_symbol} |"
                decision_tree[3] = 1
                python_tree[3] = 1
            elif python == 5:
                game_board[4] = f" {python_symbol} "
                decision_tree[4] = 1
                python_tree[4] = 1
            elif python == 6:
                game_board[5] = f"| {python_symbol}  "
                decision_tree[5] = 1
                python_tree[5] = 1
            elif python == 7:
                game_board[6] = f"  {python_symbol} |"
                decision_tree[6] = 1
                python_tree[6] = 1
            elif python == 8:
                game_board[7] = f" {python_symbol} "
                decision_tree[7] = 1
                python_tree[7] = 1
            else:
                game_board[8] = f"| {python_symbol}  "
                decision_tree[8] = 1
                python_tree[8] = 1
            
            turn = "player"
            nonlocal player_wins
            nonlocal python_wins
            #Check win
            def turn_outcome():
                nonlocal player_wins
                nonlocal python_wins
                nonlocal game_board
                nonlocal decision_tree
                nonlocal player_tree
                nonlocal python_tree
                nonlocal game_count
                
                if player_tree[0] == 1 and player_tree[1] == 1 and player_tree[2] == 1 or player_tree[3] == 1 and player_tree[4] == 1 and player_tree[5] == 1 or player_tree[6] == 1 and player_tree[7] == 1 and player_tree[8] == 1 or player_tree[0] == 1 and player_tree[3] == 1 and player_tree[6] == 1 or player_tree[1] == 1 and player_tree[4] == 1 and player_tree[7] == 1 or player_tree[2] == 1 and player_tree[5] == 1 and player_tree[8] == 1 or player_tree[0] == 1 and player_tree[4] == 1 and player_tree[8] == 1 or player_tree[2] == 1 and player_tree[4] == 1 and player_tree[6] == 1:
                    
                    player_wins += 1
                    game_count += 1
                    
                    #Reset game settings
                    game_board = ["    |","   ","|    ","    |","   ","|    ","    |","   ","|    "]
                    decision_tree = [0,0,0,0,0,0,0,0,0]
                    player_tree = [0,0,0,0,0,0,0,0,0]
                    python_tree = [0,0,0,0,0,0,0,0,0]
                    return f"😲 Amazing work, {name}! You won!"
                elif python_tree[0] == 1 and python_tree[1] == 1 and python_tree[2] == 1 or python_tree[3] == 1 and python_tree[4] == 1 and python_tree[5] == 1 or python_tree[6] == 1 and python_tree[7] == 1 and python_tree[8] == 1 or python_tree[0] == 1 and python_tree[3] == 1 and python_tree[6] == 1 or python_tree[1] == 1 and python_tree[4] == 1 and python_tree[7] == 1 or python_tree[2] == 1 and python_tree[5] == 1 and python_tree[8] == 1 or python_tree[0] == 1 and python_tree[4] == 1 and python_tree[8] == 1 or python_tree[2] == 1 and python_tree[4] == 1 and python_tree[6] == 1:
                    
                    python_wins += 1
                    game_count += 1
                    
                    #Reset game settings
                    game_board = ["    |","   ","|    ","    |","   ","|    ","    |","   ","|    "]
                    decision_tree = [0,0,0,0,0,0,0,0,0]
                    player_tree = [0,0,0,0,0,0,0,0,0]
                    python_tree = [0,0,0,0,0,0,0,0,0]
                    return f"Better luck next time {name}! 🐍 Python wins this time!"
                elif decision_tree[0] == 1 and decision_tree[1] == 1 and decision_tree[2] == 1 and decision_tree[3] == 1 and decision_tree[4] == 1 and decision_tree[5] == 1 and decision_tree[6] == 1 and decision_tree[7] == 1 and decision_tree[8] == 1:
                   
                    game_count += 1
                    #Reset game settings
                    game_board = ["    |","   ","|    ","    |","   ","|    ","    |","   ","|    "]
                    decision_tree = [0,0,0,0,0,0,0,0,0]
                    player_tree = [0,0,0,0,0,0,0,0,0]
                    python_tree = [0,0,0,0,0,0,0,0,0]
                    return f"😔 The game is tied and there are no winners this time."
                else:
                    print("Nobody has won yet, and there are still legal moves remaining. The game continues!")
                    return play_game()

                    
            
            turn_result = turn_outcome()
            print(turn_result)
            
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
                return play_game()
            else:
                print(f"\n🥳 Thank you for playing, {name}! \n\nSee you next time!")
                playagain = False
                if __name__ == "__main__":
                    sys.exit()
                else:
                    return
    return play_game


tictactoe("Shalif")

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
    
    game_instance = tictactoe(args.name)
    game_instance()
                    
            
            
            
            
            
        
        
        
        