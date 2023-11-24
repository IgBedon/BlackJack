from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.hand = []


    @abstractmethod
    def receive_card():
        pass


    @abstractmethod
    def calculate_hand():
        pass


    @abstractmethod
    def get_score(self):
        pass