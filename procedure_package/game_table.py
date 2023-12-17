import os
from poo_package.dealer import Dealer
from procedure_package import loader
from time import sleep
import inquirer

dealer = Dealer()




def start(players, players_counter, mode):
    
    print("Starting in")
    for sec in range(3):
        print(f"{sec+1}...")
        sleep(1)

    for y in range (1, players_counter+1):
        for _ in range(2):
            players["Player "+str(y)].receive_card(dealer.deal_card())

    ask_players(players, players_counter, mode)
    print("Calculating result...")
    for sec in range(3):
        print(f"{sec+1}...")
        sleep(1)
    winner = calculate_result(players, players_counter)

    if(mode == "multiplayer"):
        calculate_bet(players, winner)




def ask_players(players, players_counter, mode):
    os.system('cls')

    for x in range (1, players_counter+1):
        if(x == 2 and mode == "single"):
            pc_choices(players, x)

        else:

            while True:
                score = players["Player "+str(x)].calculate_hand()

                if(score>21):

                    print("You passed the limit! (21)")
                    if(x==players_counter+1):
                        print("Passing to the next stage...")
                    else:
                        print("Passing to the next player...")
                    for sec in range(3):
                            print(f"{sec+1}...")
                            sleep(1)
                    
                    os.system('cls')
                    break
                else:
                    questions = [
                        inquirer.List('size',
                        message="Do you want to get one more card?",
                        choices=['Yes', 'No']
                        )
                    ]

                    select = inquirer.prompt(questions)
                    match(select['size']):
                        case "Yes":
                            players["Player "+str(x)].receive_card(dealer.deal_card())
                            continue

                        case "No":
                            if(x==players_counter+1):
                                print("Passing to the next stage...")
                            else:
                                print("Passing to the next player...")

                            for sec in range(3):
                                print(f"{sec+1}...")
                                sleep(1)
                            os.system('cls')
                            break





def calculate_result(players, players_counter):
    winner_score = 0
    winner = ""

    for x in range (1, players_counter+1):
        score = players["Player "+str(x)].get_score()

        if (score <= 21 and score > winner_score):
            winner_score = score
            winner = players["Player "+str(x)].get_name()
        
    print(f"The winner is: {winner} within a score of {winner_score}!\n\n\n")

    return winner




def calculate_bet(players, winner):
    final_bet = 0
    for player in players:
        casino_chips = players[player].get_casino_chips()
        casino_chips -= players[player].get_bet()
        if(casino_chips<0):
            casino_chips = 0
        players[player].set_casino_chips(casino_chips)

        final_bet += players[player].get_bet()

        if(players[player].get_name() != winner):
            print(f"{players[player].get_name()} has {players[player].get_casino_chips()} Casino Chips left!")
        else:
            winner_player = player

    casino_chips = players[winner_player].get_casino_chips()
    casino_chips += final_bet
    players[winner_player].set_casino_chips(casino_chips)
    print(f"{players[winner_player].get_name()} is the WINNER and has received {final_bet} Chips! {players[winner_player].get_name()} has {players[winner_player].get_casino_chips()} now!\n\n\n")

    register_list = loader.register_load()
    loader.register_overwriting(players, register_list)



def pc_choices(players, player_number):
        
    while(True):
        score = players["Player "+str(player_number)].calculate_hand()
        valid_cards = []

        print("\nPC is doing it's choices")
        for sec in range(3):
            print(f"{sec+1}...")
            sleep(1)

        for card in dealer.deck:
            new_score = score + card.value
            if(new_score<=21):
                valid_cards.append(card.value)

        percentage_of_win = len(valid_cards)/len(dealer.deck)
        print(percentage_of_win)

        if(percentage_of_win>0.85):
            players["Player "+str(player_number)].receive_card(dealer.deal_card())
            print("\nPC choose to take one more card!")
            
        else:
            print("\nPC choose to not take one more card! \n")
            print("Passing to the next stage...")
            break