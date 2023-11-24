from .card import Card
import random


class Dealer:
    def __init__(self):
        self.deck = self.set_cards()

    
    def set_cards(self):
        deck = []
        for y in range (4):
            for x in range (2, 10):  
                deck.append(Card(str(x), x))

            deck.append(Card("Q", 10))
            deck.append(Card("J", 10))
            deck.append(Card("K", 10))
            deck.append(Card("A", 1))
            
        return deck


    def deal_card(self):
        random.shuffle(self.deck)
        return self.deck.pop()

        


