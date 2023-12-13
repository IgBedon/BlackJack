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
        try:
            cpf = int(input("Enter your EDV or CPF (Only numbers!): "))
            if(cpf in register_list[name][cpf]):
                print("Oh oh, someone already has this EDV or CPF!")
                continue
            break
        except:
            print("Oh oh, you have entered an invalid input!")
            continue

    return name, cpf


def add_record(register_list, name, id):
    player_data = {
        "Name":name,
        "ID":id,
        "Casino Chips": 1000 
        }

    register_list[name] = player_data
    loader.register_add(register_list)


def sign_in(register_list, players, quantity):
    players_counter = 0
    while(players_counter<quantity):
        for name in register_list:
            print(f"Name: {name}")

        account = input("Choose your account [Insert name]: ")
        try:
            players_counter += 1
            player_number = "Player "+str(players_counter)
            players[player_number] = LoggedPlayer(register_list[account]["Name"], register_list[account]["ID"], register_list[account]["Casino Chips"])
            print(register_list.get(account))
            register_list.pop(account, "Error in Pop Method")
            print()
        
        except:
            print("\nThis user isn't Signed up\n")
            players_counter -= 1

    return True, players, players_counter
        