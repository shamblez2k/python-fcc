import rps8
import guess_number
import sys

def arcade(name='PlayerOne'):     
    firstmenu = True
    
    def arcade_menu():
        nonlocal name
        nonlocal firstmenu
        if firstmenu == True:
            print(f"\n{name}, welcome to the Arcade! 🕹️")
        else:
            print(f"{name}, welcome back to the arcade menu.")

        gamechoice = input(f"\nPlease choose a game:\n1 = Rock Paper Scissors \n2 = Guess My Number \n\nOr press \"x\" to exit the Arcade.\n\n") 
   
        if gamechoice not in ["1", "2", "x"]:
            print(f"Sorry {name}, the button you\'ve pressed is not a valid option. Please select 1,2 or \"x\".\n\n")
            return arcade_menu()
        
        def game_decision(gamechoice):
            nonlocal firstmenu
            firstmenu = False
            if gamechoice == "1":
                rps_game = rps8.rps(name)
                rps_game()
                return arcade_menu()
            elif gamechoice == "2":
                guess_game = guess_number.guess_number(name)
                guess_game()
                return arcade_menu()
            else:
                print(f"See you next time!\nBye {name}! 😊")
                sys.exit()
        game_decision(gamechoice)
    
    
            
    return arcade_menu

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
    
    arcade_instance = arcade(args.name)
    arcade_instance()

 