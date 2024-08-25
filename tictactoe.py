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
    turn_counter = 0
    
    def decide_turn():
        nonlocal name, turn, player_symbol, python_symbol
        player = int(input(f"Hi {name}!\nPick 1 for heads or 2 for tails.\n"))
        if player == 1:
            print("You picked heads!")
        else:
            print("You picked tails!")
        decision = int(random.choice("12"))
        if decision == 1:
            print("Heads goes first!")
        else:
            print("Tails goes first!")
        if player == decision:
            print(f"🥳 Congratulations {name}! You'll go first, so you are x!\n")
            turn = "player"
            player_symbol = "x"
            python_symbol = "o"
        else:
            print("Python goes first, it is x!\n")
            turn = "python"
    
    decision_tree = [0,0,0,0,0,0,0,0,0]
    player_tree = [0,0,0,0,0,0,0,0,0]
    python_tree = [0,0,0,0,0,0,0,0,0]
    
    game_board = ["   ","   ","   "] * 3
    
    
    def display_board():
        print(f"{game_board[0]} |{game_board[1]}| {game_board[2]}\n=============\n{game_board[3]} |{game_board[4]}| {game_board[5]}\n=============\n{game_board[6]} |{game_board[7]}| {game_board[8]}")

    def check_winner(tree, player_name):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]
        for condition in win_conditions:
            if all(tree[i] == 1 for i in condition):
                return True
        return False
    
    def play_game():
        nonlocal turn, turn_counter, player_wins, python_wins, name
        
        if turn_counter == 0:
            decide_turn()
        
        while turn_counter < 9:
            display_board()
        
            if turn_counter == 0:
                print(f"\n😁 Hello {name}!\nLet\'s play a game of tic-tac-toe. Please Enter a number corresponding to the empty spaces available, as shown above. \n1 for top-left, \n2 for top-middle,\n3 for top-right,\n4 for middle-left, \n5 for middle-middle,\n6 for middle-right,\n7 for bottom-left, \n8 for bottom-middle,\n9 for middle-right: \n\n")
    
            
            if turn == "player":        
                playerchoice = input("It is your turn. Please enter your choice:\n")
            
                if playerchoice not in "123456789" or decision_tree[int(playerchoice)-1] != 0:
                    print(f"Sorry, {name}, you must enter a valid choice.\nPlease enter a number between 1 and 9, based on the key given earlier.")
                    continue
                    
                player_move = int(playerchoice) - 1
                game_board[player_move] = f" {player_symbol} "
                decision_tree[player_move] = 1
                player_tree[player_move] = 1
                print(f"You chose {playerchoice}:\n")
                    
                if check_winner(player_tree, name):
                    player_wins += 1
                    display_board()
                    print(f"\n😲 Amazing work, {name}! You won!")
                    break
                turn = "python"
            else:
                print(f"It is Python\'s turn.")
                while True:
                    computerchoice = int(random.choice("123456789")) - 1
                    if decision_tree[computerchoice] == 0:
                        break
                
                print(f"Python chose {computerchoice}:\n")
                game_board[computerchoice] = f" {python_symbol} "
                decision_tree[computerchoice] = 1
                python_tree[computerchoice] = 1   
                
                if check_winner(python_tree, "Python"):
                    python_wins += 1
                    display_board()
                    print(f"\nBetter luck next time {name}! 🐍 Python wins this time!")
                    break
                turn = "player"
            
            turn_counter += 1
        
        if turn_counter == 9:
            print("😔 The game is tied and there are no winners this time.")
            
        print(f"\nPlay again, {name}?")
        while True:
            playagain = input("\nY for Yes or \nN for No \n")
            if playagain.lower() not in ["y","n"]:
                continue
            else:
                break
        
        if playagain.lower() == "y":
            return tictactoe(name)
        else:
            print(f"\n🥳 Thank you for playing, {name}! \n\nSee you next time!")
            playagain = False
            if __name__ == "__main__":
                sys.exit()
            else:
                return
                
    return play_game()


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
    game_instance
                    
            
            
            
            
            
        
        
        
        