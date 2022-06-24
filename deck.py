class Deck:

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    picked_cards = []

    def reset_deck(self):
        self.cards.extend(self.picked_cards)
        self.picked_cards.clear()
