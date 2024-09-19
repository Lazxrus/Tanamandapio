# something travel to diff world, find a way out but this time it's actually quite easy to do and you go back to earth only to find it has been destroyed, ravaged and filled with (not known[monster]) nothing is the same, you then notice something coming at you fast you cant make up its shape[what do you do?], after dodging the thing you dodge,choice system, different outcome per choice, 

# Checks to see if there is progress for the main menu options, that's all I'd use it for
def check_progress(game_progress):
    return len(game_progress) > 0

def get_user_choice():
    valid_choices = {1, 2, 3, 4}
    while True:
        choice = input("Choose an option: ")
        if choice in valid_choices:
            return choice
        else:
            print("Please enter a valid choice!")

#main menu in dictionary so it's more manageable
def main_menu(game_progress):
    menu_options = {
        2: "Start a new game",
        3: "Options",
        4: "Quit Game"
    }

    if check_progress(game_progress):
        menu_options[1] = "Continue"

    print("\n====Tanamandapio====")
    for key, value in sorted(menu_options.items()):
        print(f"{key}. {value}")
    print("======================")

    return menu_options


def main():
    game_progress = {}
    while True:
        menu_options = main_menu(game_progress)
        choice = get_user_choice(set(menu_options.keys()))

        choice_actions = {
            1: lambda: continue_game(game_progress) if "Continue" in menu_options.values() else None,
            2: lambda: new_game(),
            3: lambda: options_menu(game_progress),
            4: quit_game
        }

        action = choice_actions.get(choice)
        if action: 
            result = action()
            if result is not None:
                game_progress = result

            else:
                print("Invalid choice. Please try again.")


def update_progress(game_progress, key, value):
    game_progress[key] = value
    return game_progress

def new_game(game_progress):
    game_progress = {}
    player_name = input("What's your name?")
    game_progress = update_progress(game_progress, 'player_name', player_name)
    game_progress = update_progress(game_progress, 'health', 1)
    game_progress = update_progress(game_progress, 'inventory', {})
    game_progress = update_progress(game_progress, 'location', 'start_area1')
    
    print("Initial story jargon")
    # Present initial choice here

    return game_progress

def continue_game(game_progress):
    # Implement game loop here
    pass

def text_output:
    print("Welcome to Tanamandapio")

# progress dependant items
def item_list(): 
    weapon_list = {
        'stick',
        'broken stick',
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

def options_menu(game_progress):
    while True:
        print("Options")
        print("1. Adjust Text Speed")
        print("2. Change Player Name")
        print("3. Return to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            adjust_text_speed()
        elif choice == '2':
            game_progress = change_player_name(game_progress)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again")

def adjust_text_speed():
    while True:
        
    pass


def change_player_name(game_progress):
    new_name = input("Enter player name: ")
    game_progress['player_name'] = new_name
    print(f"Player name changed to {new_name}")
    return game_progress


if __name__ == "__main__":
    main()