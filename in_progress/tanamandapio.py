# something travel to diff world, find a way out but this time it's actually quite easy to do and you go back to earth only to find it has been destroyed, ravaged and filled with (not known[monster]) nothing is the same, you then notice something coming at you fast you cant make up its shape[what do you do?], after dodging the thing you dodge,choice system, different outcome per choice, 



# main menu options, define progress
def main_menu():
    print("\n====Tanamandapio====")
    if progress:
        print("1. Continue")
    else:
        print(" ")
    print("2. Start a new game")
    print("3. Options")
    print("4. Quit Game")
    print("========================")

# Mistify later 
def get_user_choice():
    valid_choices = {'1', '2', '3', '4'}
    while True:
            choice = int(input("Choose an option: "))
            if choice in valid_choices:
                return choice
            else:
                print("Please enter a valid choice!")

# I don't think it's all wrong, but I don't think it's doing what I want it to do.
def main():
    game_progress = []
    while True:
        main_menu()
        choice = get_user_choice()
        if choice == '1':
            continue_game(game_progress)
        elif choice == '2':
            new_game(game_progress)
        elif choice == '3':
            options_menu(game_progress)
        elif choice == '4':
            confirm = input("Are you sure you want to exit?(y/n): ").lower()
            if confirm == 'y':
                print("Exit message")
                break
            elif confirm == 'n':
                print("Funny exit message")
            else:
                print("Invalid Input.")




def continue_game(game):
# This function should handle the main gameplay loop.
# How will you structure the story progression?
# Consider using a loop to keep the game running until an end condition is met.

def new_game(game):
    get_name = []
    while True:
        get_name = input("Who are you?")
        for index in get_name:
            return current_location
        else:
            print("Enter a valid name")
        health = 5
        inventory = {
            
        }
        abilities = {
            
        }
        level = 1
        current_location = start_area1
        progress = 
# Think about what needs to happen when starting a new game.
# Consider initializing player stats, inventory, and story progress.
# How will you introduce the game's story and setting?


def options_menu(game):
# What settings or options might your game need?
# Think about how to display these options to the user.
# How will you handle saving changes to these options?

# progress dependant items
def item_list(): 
    weapon_list = {
        'metal_pipe', 
        'knife', 
        'arrow', 
        'crossbow', 
        'pistol'
    }

def inventory():
    player_inventory = {
        # access the dictionary see items available to the player, based on progress?
    }

def abilities():
    abilities_list = {
        # access dictionary upon initialization?, based on progress
    }

def locations():
    locations = {
        "start_area1": "Portal",
        
    }


def what_happens_when_game_starts


if __name__ == "__main__":
    main()