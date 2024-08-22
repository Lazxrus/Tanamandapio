# something travel to diff world, find a way out but this time it's actually quite easy to do and you go back to earth only to find it has been destroyed, ravaged and filled with (not known[monster]) nothing is the same, you then notice something coming at you fast you cant make up its shape[what do you do?], after dodging the thing you dodge,choice system, different outcome per choice, 

# Checks to see if there is progress for the main menu options, that's all I'd use it for
def check_progress(game_progress):
    return len(game_progress) > 0

def get_user_choice(valid_choices):
    while True:
        choice = int(input("Choose an option: "))
        if choice in valid_choices:
            return choice
        else:
            print("Please enter a valid choice!")

# main menu options, define progress
def main_menu(game_progress):
    print("\n====Tanamandapio====")
    if check_progress(game_progress):
        print("1. Continue")
    else:
        print(" ") # Could print something different
    print("2. Start a new game")
    print("3. Options")
    print("4. Quit Game")
    print("========================")

# I don't think it's all wrong, but I don't think it's doing what I want it to do.
def main():
    game_progress = [] #correct
    while True:
        main_menu(game_progress)
        valid_choice = {'1', '2', '3', '4'}
        choice = get_user_choice(valid_choice)
        if choice == '1' and check_progress(game_progress):
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
                print("Funny coming return message")
            else:
                print("Invalid Input.")



def new_game(game_progress):
    player_name = {[]}
    while True:
        try:
            player_name = input("What's your name?")
            break
        except TypeError:
            print("Invalid input")
    health = 1
    inventory = {}
    starting_locations = {'start_area1'}
    print("Initial story jargan")
    # present a decision all progress is returned to the empty list game_progress = []
    # return continue_game?
    # create a separate function for progress, in it make everything return to game_progress, and every action and dictionary calls that function?
    # for transitions try return and pass?

def text_output:
    print("Welcome to Tanamandapio")

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

if __name__ == "__main__":
    main()