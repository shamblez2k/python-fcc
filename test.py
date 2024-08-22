
print(f"    |   |    \n=============\n    |   |   \n=============\n    |   |   \n")

choice = int(input("Make selection"))

# game_board = {
#     "top-left": "    |",
#     "top-middle": "   ",
#     "top-right": "|    ",
#     "mid-left": "    |",
#     "mid-middle": "   ",
#     "mid-right": "|    ",
#     "bottom-left": "    |",
#     "bottom-middle": "   ",
#     "bottom-right": "|    ",
# }
 
game_board = ["  x |"," x ","|    ","    |","   ","|    ","    |","   ","|    "]

if choice == 1:
    game_board[2] = "| x  "
    
print(f"{game_board[0]}{game_board[1]}{game_board[2]}\n=============\n")

        # class gamebox(Enum):
        #     TOP_lEFT        = 1
        #     TOP_MIDDLE      = 2
        #     TOP_RIGHT       = 3
        #     MIDDLE_LEFT     = 4
        #     MIDDLE_MIDDLE   = 5
        #     MIDDLE_RIGHT    = 6
        #     BOTTOM_LEFT     = 7
        #     BOTTOM_MIDDLE   = 8
        #     BOTTOM_RIGHT    = 9