import json

def register_load():
    # Checking if JSON already exists and loading it
    try:
        with open ("register_file.json", "r", encoding="UTF-8") as register_file:
            if register_file:
                registered = json.load(register_file)
            else:
                print("\n=================================\nWe don't have data stored yet!\n=================================\n")
                return {}
        return registered
    except FileNotFoundError:
        return {}
    

def register_add(register_list):
    # Writing in JSON to save data
    with open ("register_file.json", "w", encoding="UTF-8") as register_file:
        json.dump(register_list, register_file, ensure_ascii=False, indent=4)


def register_overwriting(players, register_list):
    # Overwriting data after the game
    for player in players:
        name = players[player].get_name()

        casino_chips = players[player].get_casino_chips()
        if(casino_chips<=0):
            register_list.pop(name, "Error in Pop Method")
        else:
            register_list[name]["Casino Chips"] = players[player].get_casino_chips()

    with open ("register_file.json", "w", encoding="UTF-8") as register_file:
        json.dump(register_list, register_file, ensure_ascii=False, indent=4)