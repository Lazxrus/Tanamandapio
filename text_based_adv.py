# something travel to diff world, find a way out but this time it's actually quite easy to do and you go back to earth only to find it has been destroyed, ravaged and filled with (not known[monster]) nothing is the same, you then notice something coming at you fast you cant make up its shape[what do you do?], after dodging the thing you dodge

# choice system, different outcome per choice, 

def game_menu():
    print("\n====Tanamandapio====")
    print("1. Continue")
    print("2. Start a new game")
    print("3. Options")
    print("4. Quit Game")
    print("========================")

def get_user_choice():
    valid_choices = {'1', '2', '3', '4'}
    while True:
            choice = int(input(" "))
            if choice in valid_choices:
                return choice
            else:
                print("Please enter a valid choice!")

def main():
    game = []
    while True:
        game_menu()
        choice = get_user_choice()
        if choice == '1':
            continue_game(game)
        elif choice == '2':
            new_game(game)
        elif choice == '3':
            options_menu(game)
        elif choice == '4':
            print("Are you sure?")
            print("You live to die another day")
            break
        else:
            print("You dare toy with the ancients?")

def continue_game(game):

def new_game(game):


def options_menu(game):
    print("Text Speed")
    for 
    print("Brightness")

def chapter_1():


def scene_1():
    print("You wake up confused, in an unfamiliar land full of mystic beings and countryside smells, tall grass all around moving ferociously given the strong winds")
    print("You look down and notice a strange bug holding onto your hand")


def user_decision_scene1():
    


def item_list():
    items = {

    }

def locations():
    locations = {

    }


if __name__ == "__main__":
    main()