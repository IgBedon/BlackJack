from . import register, loader, game_table
from poo_package.not_logged_player import NotLoggedPlayer
import inquirer


def introduction():
    print("Welcome to our Casino!")
    print("We're gonna play 21, the card game! The goal is to be the closest of 21.\nYou'll choose if you'll stop or continue taking cards")
    print("\n------------------------------------------------------------------\n")
    
    
def catch_choice():
    questions = [
        inquirer.List('size',
        message="Do you want to...",
        choices=['Sign Up', 'Sign In', 'Play against PC without account', 'Exit'],
        )
    ]

    select = inquirer.prompt(questions)
    match(select['size']):
        case "Sign Up":
            return 1
        case "Sign In":
            return 2
        case "Play against PC without account":
            return 3
        case "Exit":
            return 4
        

def menu_choice(choice, register_list, players):
    match(choice):
        case 1:
            name, id = register.sign_up(register_list)

            if(name == ""):
                return

            register.add_record(register_list, name, id)
            print()

        case 2:
            stop = False

            if(not register_list):
                print("We don't have users signed up yet.")
                choice = catch_choice()
                return menu_choice(choice, register_list)
            else:
                while(True):
                    try:
                        quantity = int(input("How many players?\n"))
                        if(quantity == 1):
                            print("You must have more than 1 player!")
                            continue
                        else:
                            while(not stop):
                                stop, players, players_counter = register.sign_in(register_list, players, quantity)
                            break
                    except:
                        print("Invalid value!")

            game_table.start(players, players_counter)

        case 3:
            players["Player 1"] = NotLoggedPlayer("Random Player")
            players["Player 2"] = NotLoggedPlayer("PC")
            game_table.start(players, 2)

        case 4:
            print("Well, if you want... Finishing...")
            exit()


def start():
    introduction()
    while(True):
        players = {}
        register_list = loader.register_load()
        choice = catch_choice()
        menu_choice(choice, register_list, players)

