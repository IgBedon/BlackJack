import json

def register_load():
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
    with open ("register_file.json", "w", encoding="UTF-8") as register_file:
        register_list = json.dump(register_list, register_file, ensure_ascii=False, indent=4)