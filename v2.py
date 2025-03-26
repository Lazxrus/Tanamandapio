def check_progress(game_progress):
    """Checks if there is any progress in the game (for enabling 'Continue' option)."""
    return bool(game_progress)

def get_user_choice(valid_choices):
    """Gets user input and ensures it is a valid option."""
    while True:
        try:
            choice = int(input("Choose an option: "))
            if choice in valid_choices:
                return choice
            else:
                print("Invalid choice. Please enter a valid option.")
        except ValueError:
            print("Please enter a number.")

def main_menu(game_progress):
    """Displays the main menu and returns the selected menu option."""
    menu_options = {
        2: "Start a new game",
        3: "Options",
        4: "Quit Game"
    }

    if check_progress(game_progress):
        menu_options[1] = "Continue"

    print("\n==== Tanamandapio ====")
    for key, value in sorted(menu_options.items()):
        print(f"{key}. {value}")
    print("======================")

    return menu_options

def main():
    """Main loop for the game menu."""
    game_progress = {}  # This will hold player progress

    while True:
        menu_options = main_menu(game_progress)
        choice = get_user_choice(set(menu_options.keys()))

        # Mapping menu choices to functions
        choice_actions = {
            1: lambda: continue_game(game_progress) if "Continue" in menu_options.values() else None,
            2: lambda: new_game(),
            3: lambda: options_menu(game_progress),
            4: quit_game
        }

        action = choice_actions.get(choice)
        if action: 
            result = action()
            if isinstance(result, dict):  # Ensures game_progress is updated if needed
                game_progress = result
        else:
            print("Invalid choice. Please try again.")

def update_progress(game_progress, key, value):
    """Updates the game progress dictionary."""
    game_progress[key] = value
    return game_progress

def new_game():
    """Starts a new game by resetting game progress."""
    game_progress = {}
    player_name = input("Enter your name: ")
    game_progress = update_progress(game_progress, 'player_name', player_name)
    game_progress = update_progress(game_progress, 'health', 1)
    game_progress = update_progress(game_progress, 'inventory', {})
    game_progress = update_progress(game_progress, 'location', 'start_area1')

    print("\nStarting a new journey...")
    print("You wake up in an unfamiliar world...\n")

    return game_progress

def continue_game(game_progress):
    """Handles continuing an existing game (currently a placeholder)."""
    print("Continuing game...")
    # Implement actual game logic here
    return game_progress

def quit_game():
    """Exits the game."""
    print("Exiting the game. Goodbye!")
    exit()

def options_menu(game_progress):
    """Displays and handles the options menu."""
    while True:
        print("\n==== Options ====")
        print("1. Adjust Text Speed")
        print("2. Change Player Name")
        print("3. Return to Main Menu")
        print("=================")
        
        choice = get_user_choice({1, 2, 3})
        
        if choice == 1:
            adjust_text_speed()
        elif choice == 2:
            game_progress = change_player_name(game_progress)
        elif choice == 3:
            return  # Return to main menu

def adjust_text_speed():
    """Adjusts text speed for displaying dialogue (currently a placeholder)."""
    print("\nText speed adjustment not implemented yet.")
    # Could add options like slow, normal, fast here

def change_player_name(game_progress):
    """Allows the player to change their in-game name."""
    new_name = input("Enter new player name: ")
    game_progress['player_name'] = new_name
    print(f"Player name changed to {new_name}")
    return game_progress

if __name__ == "__main__":
    main()
