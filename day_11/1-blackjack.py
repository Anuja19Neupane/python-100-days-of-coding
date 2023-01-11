# suruma hamile card ko list banaunu parxa
import random


def deal_card():
    # ace act as 1 or 11 according toyour desire    card = random.choice(cards)
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return card


def calculate_score(cards):


user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):  # 0 and 1
    new_card = deal_card()
    # list ko thau ma single item use garnu parney xa vaney use append
    user_cards.append(new_card)
    # append le single item lai list ma add garxa
    computer_cards.append(deal_card())
user_score = -calculate_score(user_cards)
compueter_scores = calculate_score(computer_cards)
print(f"your cards:{user_cards},current score:{user_score} ")
print(f"computer's first card:{computer_cards[0]}")

if user_score == 0 or compueter_scores == 0 or user_score > 21:
    is_game_over = True

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
