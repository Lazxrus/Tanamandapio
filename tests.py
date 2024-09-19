def check_progress(game_progress):
    return len(game_progress) > 0

def get_user_choice(self):
    valid_choices = {1, 2, 3, 4}
    while True:
        choice = input("Choose an option: ")
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
    game_progress = {}
    valid_choices = {1, 2, 3, 4}
    while True:
        main_menu(game_progress)
        choice = get_user_choice(valid_choices)
        if choice == 1 and check_progress(game_progress):
            continue_game(game_progress)
        elif choice == 2:
            game_progress = new_game() # new_game creates and returns a new game state
        elif choice == 3:
            options_menu(game_progress)
        elif choice == 4:
            confirm_exit = input("Are you sure you want to exit?(y/n): ").lower()
            if confirm_exit == 'y':
                print("Exit message")
                break
            elif confirm_exit == 'n':
                print("Funny coming return message")

            else:
                print("Invalid Input.")

if __name__ == "__main__":
    main()