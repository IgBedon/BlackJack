import os
from poo_package.dealer import Dealer
from procedure_package import loader
from time import sleep
import inquirer


def start(players, players_counter, mode):
    # Inicializing Dealer before start some game
    dealer = Dealer()

    print("Starting in")
    for sec in range(3):
        print(f"{sec+1}...")
        sleep(1)

    # Giving cards
    for y in range (1, players_counter+1):
        for _ in range(2):
            players["Player "+str(y)].receive_card(dealer.deal_card())

    # Asking for card choice
    ask_players(players, players_counter, mode, dealer)
    print("Calculating result...")
    for sec in range(3):
        print(f"{sec+1}...")
        sleep(1)

    # Defining winners
    winners = calculate_result(players, players_counter)

    # if you are logged, this will calculate bets
    if(mode == "multiplayer"):
        calculate_bet(players, winners)




def ask_players(players, players_counter, mode, dealer):
    os.system('cls')

    # Asking for all players or redirecting to computer choices
    for x in range (1, players_counter+1):
        if(x == 2 and mode == "single"):
            pc_choices(players, x, dealer)

        else:

            while True:
                score = players["Player "+str(x)].calculate_hand()

                # Defining if we will have the opportunity to take one more card
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

                    # Prompt to decide if you will get one more card
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
    highest_score = 0
    winners = []
    
    # Defining the highest score.
    for x in range(1, players_counter + 1):
        score = players["Player " + str(x)].get_score()

        if score <= 21:
            if score > highest_score:
                highest_score = score
                winners = [players["Player " + str(x)].get_name()]
            elif score == highest_score:
                winners.append(players["Player " + str(x)].get_name())

    # It checks if we have more than one person with the same score (Highest Score)
    if not winners:
        print("Oh no, no one wins!")
    else:
        if len(winners) == 1:
            print(f"The winner is: {winners[0]} with a score of {highest_score}!\n")
        else:
            print(f"It's a tie! Players with the highest score ({highest_score}): {', '.join(winners)}!\n")

    return winners





def calculate_bet(players, winners):

    # Show the result if no one have a valid score
    if not winners:
        print("Returning bets to players...\n")

        for player in players:
            print(f"{players[player].get_name()} has {players[player].get_casino_chips()} Casino Chips now!")
        print()

    # Show the result if only one person won
    elif(len(winners) == 1):
        final_bet = 0

        # Getting Player's bet and recalculating casino Chips. Decreasing if the player lost and increasing of the player won
        for player in players:
            casino_chips = players[player].get_casino_chips()
            casino_chips -= players[player].get_bet()
            if(casino_chips<0):
                casino_chips = 0
            players[player].set_casino_chips(casino_chips)

            final_bet += players[player].get_bet()

            for winner in winners:
                if(players[player].get_name() != winner):
                    print(f"{players[player].get_name()} has {players[player].get_casino_chips()} Casino Chips left!")
                else:
                    winner_player = player

        casino_chips = players[winner_player].get_casino_chips()
        casino_chips += final_bet
        players[winner_player].set_casino_chips(casino_chips)
        print(f"{players[winner_player].get_name()} is the WINNER and has received {final_bet} Chips! {players[winner_player].get_name()} has {players[winner_player].get_casino_chips()} now!\n\n")

    else:
        winners_number = []
        pot = 0
        
        # Setting the winners to calculate Casino Chips
        for player in players:
            pot += (players[player].get_bet())
            if(players[player].get_name() in winners):
                winners_number.append(player)

        # Getting Player's bet and recalculating casino Chips. Decreasing if the player lost and increasing of the player won
        for player in players:
            casino_chips = players[player].get_casino_chips()
            casino_chips -= players[player].get_bet()
            if(casino_chips<0):
                casino_chips = 0
            players[player].set_casino_chips(casino_chips)

            if(player not in winners_number):
                print(f"{players[player].get_name()} has {players[player].get_casino_chips()} Casino Chips now!")
        print()

        # Showing the result if we have more than one player
        print("It's a tie, so we're going to divide the pot among the winners...")
        for player_number in winners_number:
            casino_chips = players[player_number].get_casino_chips()
            casino_chips += pot // len(winners)
            players[player_number].set_casino_chips(casino_chips)
            print(f"{players[player_number].get_name()} has received {pot // len(winners)} Chips! {players[player_number].get_name()} has {players[player_number].get_casino_chips()} now!")
        print()

    # Saving the result
    register_list = loader.register_load()
    loader.register_overwriting(players, register_list)



def pc_choices(players, player_number, dealer):
        
    while(True):
        score = players["Player "+str(player_number)].calculate_hand()
        valid_cards = []

        print("\nPC is doing it's choices")
        for sec in range(3):
            print(f"{sec+1}...")
            sleep(1)

        # Calculating probability to receive a valid card
        for card in dealer.deck:
            new_score = score + card.value
            if(new_score<=21):
                valid_cards.append(card.value)

        # Calculating
        percentage_of_win = len(valid_cards)/len(dealer.deck)
        print(percentage_of_win)

        if(percentage_of_win>0.85):
            players["Player "+str(player_number)].receive_card(dealer.deal_card())
            print("\nPC choose to take one more card!")
            
        else:
            print("\nPC choose to not take one more card! \n")
            print("Passing to the next stage...")
            break