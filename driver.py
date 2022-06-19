from player import Player

user = Player()
computer = Player()


def play_game():
    is_game_over = 'n'
    for i in range(2):
        user.deal()
        computer.deal()
    computer.calculate_score()
    while is_game_over == 'n':
        user.calculate_score()
        print(f"Your cards: {user.cards}, current score: {user.score}")
        print(f"Computer's first card: {computer.cards[0]}")
        if user.score == 0 or computer.score == 0 or user.score > 21:
            is_game_over = 'y'
        else:
            deal_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if deal_choice == 'y':
                user.deal()
            else:
                is_game_over = 'y'
    while computer.score != 0 and computer.score < 17:
        computer.deal()
        computer.calculate_score()
    print(f'Computer cards: {computer.cards}, computer score: {computer.score}')
    user.compare_score_to(computer)


begin_choice = 'y'
while begin_choice == 'y':
    begin_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if begin_choice == 'y':
        play_game()
