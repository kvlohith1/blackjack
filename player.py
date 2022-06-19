import random


class Player:

    def __init__(self):
        self.deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.cards = []
        self.score = 0

    def deal(self):
        self.cards.append(random.choice(self.deck))

    def calculate_score(self):
        if sum(self.cards) == 0 and len(self.cards) == 2:
            self.score = 0
        elif sum(self.cards) > 21 and 11 in self.cards:
            self.cards.remove(11)
            self.cards.append(1)
            self.score = sum(self.cards)
        else:
            self.score = sum(self.cards)

    def compare_scores(self, opponent):
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
