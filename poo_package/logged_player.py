from .player import Player


class LoggedPlayer(Player):

    def __init__(self, name, id, casino_chips):
        super().__init__()
        self.__name = name
        self.__id = id
        self.__casino_chips = casino_chips
        self.__score = 0


    def receive_card(self, card):
        self.hand.append(card)

    
    def calculate_hand(self):
        self.__score = 0
        print(f"{self.__name} - Your cards are: ")
        for card in self.hand:
            print(card.value)
            self.__score += card.value
            
        print(f"Your score is: {self.__score}")
        return self.__score
    

    def get_score(self):
        return self.__score
    
    def get_name(self):
        return self.__name