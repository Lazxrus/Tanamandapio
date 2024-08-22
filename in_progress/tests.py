def main_menu():
    print("\n====Tanamandapio====")
    print("1. Continue")
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

def new_game(game_progress):
    player_name = []
    while True:
        try:
            player_name = input("What's your name?")
            break
        except ValueError:
            print("Invalid input")
    health = 1
    inventory = {'empty'}
    starting_locations = {'start_area1'}
    print("Initial story jargan")
    # present a decision all progress is returned to the empty list game_progress = []
    # return continue_game?
    # create a separate function for progress, in it make everything return to game_progress, and every action and dictionary calls that function?
    # for transitions try return and pass?

def progress(game_progress):
    progress = []
    return new_game

if __name__ == "__main__":
    main()