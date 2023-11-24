import os
from poo_package.dealer import Dealer
from time import sleep
import inquirer

dealer = Dealer()

def start(players, players_counter):
    for y in range (1, players_counter+1):
        for _ in range(2):
            players["Player "+str(y)].receive_card(dealer.deal_card())

    ask_players(players, players_counter)
    print("Calculating result...")
    for sec in range(3):
        print(f"{sec+1}...")
        sleep(1)
    calculate_result(players, players_counter)

def ask_players(players, players_counter):
    os.system('cls')
    for x in range (1, players_counter+1):

        if(players["Player "+str(x)] == players["Player 2"]):
            pc_choices()

        while True:
            score = players["Player "+str(x)].calculate_hand()

            if(score>21):
                print("You passed the limit! (21)")
                if(x==players_counter+1):
                    print("Passing to the next stage...")
                else:
                    print("Passing to the next player...")
                for sec in range(5):
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
                        print("Passing to the next player...")
                        for sec in range(5):
                            print(f"{sec+1}...")
                            sleep(1)
                        os.system('cls')
                        break


def calculate_result(players, players_counter):
    winner_score = 0
    winner = ""
    for x in range (1, players_counter+1):
        score = players["Player "+str(x)].get_score()
        if (score < 21 and score > winner_score):
            winner_score = score
            winner = players["Player "+str(x)].get_name()
        
    print(f"The winner is: {winner} within a score of {winner_score}!\n\n\n")


def pc_choices():
    print("PC is doing it's choices")
    for sec in range(5):
            print(f"{sec+1}...")
            sleep(1)