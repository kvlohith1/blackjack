import random
from deck import Deck


class Player:

    def __init__(self):
        self.cards = []
        self.score = 0

    def deal(self):
        picked_card = random.choice(Deck.cards)
        self.cards.append(picked_card)
        Deck.cards.remove(picked_card)

    def calculate_score(self):
        if sum(self.cards) == 0 and len(self.cards) == 2:
            self.score = 0
        elif sum(self.cards) > 21 and 11 in self.cards:
            self.cards.remove(11)
            self.cards.append(1)
            self.score = sum(self.cards)
        else:
            self.score = sum(self.cards)

    def compare_score_to(self, opponent):
        if self.score > 21 and opponent.score > 21:
            print('You went over, you lose.')
        elif opponent.score > 21:
            print('Computer went over. You win.')
        elif self.score > 21:
            print('You went over, you lose.')
        elif self.score == opponent.score:
            print('Draw')
        elif self.score > opponent.score:
            print('You win.')
        elif self.score < opponent.score:
            print('Computer wins')
