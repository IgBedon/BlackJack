from .player import Player


class NotLoggedPlayer(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.__score = 0
    
    
    def get_score(self):
        return self.__score
    
    
    def get_name(self):
        return self.name


    def receive_card(self, card):
        self.hand.append(card)

    
    def calculate_hand(self):
        self.__score = 0
        print(f"{self.name} - Your cards are: ")
        for card in self.hand:
            print(card.value)
            self.__score += card.value
            
        print(f"Your score is: {self.__score}")
        return self.__score
