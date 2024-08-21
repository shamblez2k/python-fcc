# Closure is a function having access to the scope of its parent function after the parent function has returned


def parent_function(person, coins):
    #coins = 3
    
    def play_game():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")
    
    return play_game

tommy = parent_function("Tommy", 4)
jenny = parent_function("Jenny", 3)

tommy()
tommy()

jenny()

tommy()

#Closures are a good way to avoid creating global variables when we need to access variables in a nested function from it's parent function