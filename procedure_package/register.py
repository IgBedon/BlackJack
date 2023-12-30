from poo_package.logged_player import LoggedPlayer
from procedure_package import loader


def sign_up(register_list):
    print("This is the Sign Up page!")
    while(True):
        try:
            name = input("Enter your name: ").title()
            if(name in register_list):
                print("\nOh oh, you are already signed up!\n")
                return "", 0
            break
        except:
            print("Oh, you have entered an invalid input!")
            continue

    while(True):
        validation = True
        try:
            cpf = int(input("Enter your EDV or CPF (Only numbers!): "))

            for key in register_list:
                if (register_list[key]["ID"] == cpf):
                    print("Oh oh, someone already has this EDV or CPF!\n")
                    validation = False
                    break
            if(not validation):
                continue

            print("\nRegistered!")
            break
        except:
            print("Oh oh, you have entered an invalid input!\n")
            continue

    return name, cpf


def add_record(register_list, name, id):
    # Separating in a dictionary to save in JSON
    player_data = {
        "Name":name,
        "ID":id,
        "Casino Chips": 1000 
        }

    register_list[name] = player_data
    loader.register_add(register_list)


def sign_in(register_list, players, quantity):
    players_counter = 0

    # Method to Choose your player
    while(players_counter<quantity):
        for name in register_list:
            print(f"Name: {name}")

        account = input("Choose your account [Insert name] or Enter 'Exit' to return: \n").title()

        if(account.title() == "Exit"):
            print()
            return True, {}, 0

        players_counter += 1

        # Setting the player like Player 1, Player 2...
        player_number = "Player "+str(players_counter)

        # Verification of account is registered and getting bet informations
        if(account in register_list):
            print(f"\nYou have {register_list[account]['Casino Chips']} Casino Chips!")

            while(True):
                try:
                    bet = int(input("Enter the amount of chips you want to bet: "))
                    if(bet <= register_list[account]["Casino Chips"] and bet >= 0):
                        players[player_number] = LoggedPlayer(register_list[account]["Name"], register_list[account]["ID"], register_list[account]["Casino Chips"], bet)
                        print(f"\nName: {register_list[account]['Name']} \nID: {register_list[account]['ID']} \nCasino Chips after Bet: {(register_list[account]['Casino Chips']-bet)} \nBet: {bet} Chips!")
                        print("\n====================================================================")
                        print("\nOk, you're ready!\n")
                        print("====================================================================\n")

                        register_list.pop(account, "Error in Pop Method")

                        break
                    else:
                        print("You don't have enough Chips!\n")
                except:
                    print("This isn't a valid input!\n")
        else:
            print("\nThis user isn't Signed up\n")
            players_counter -= 1

    return True, players, players_counter
        