import random

possible_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_card(from_cards: list, n: int):

    choosen = random.sample(from_cards, n)
    for i in choosen:
        # hamile choose garisakeko card possible card bata removegarney cuz it won't repeat.
        from_cards.remove(i)
    return choosen


# my_card ma get_card ko possible_card bata 2ota value liii
my_cards = get_card(possible_cards, 2)
computer_cards = get_card(possible_cards, 2)

finish = False
victory = False
turn = "human"
while not finish:
    if turn == "human":
        print(my_cards)
        choice = input(
            "Do you want one more card? type 'y' for yes and 'n' for no:")
        if choice == "y":
            # yedi user le ajhei euta card lina prefer garxa vaney,
            next_card = get_card(possible_cards, 1)
            my_cards += next_card  # tyo paxi leko card lai next_card ko name deko xa
            if sum(my_cards) > 21:
                finish = True

        else:
            finish = True
            if sum(my_cards) > sum(computer_cards):
                win = True
        turn = "computer"

    else:
        next_card = get_card(possible_cards, 1)
        computer_cards += next_card
        if sum(computer_cards) > 21:
            print("computer lose")
            finish = True
            victory = True
        elif(sum(computer_cards) == 21):
            victory = "False"

        turn = "my"


if victory:
    print("winner")
else:
    print("loser")
print(f"computer cards: {computer_cards} and my cards: {my_cards}")
