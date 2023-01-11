import random
# set global variable
easy_level_turn = 10
hard_level_turn = 5


def check_answer(guess, random_integer, turn):
    """ checks answer against guess. returns the number remaining.  """
    if guess > random_integer:
        print("your guess is too high.")
        return turn-1
    elif guess < random_integer:
        print("your guess is too low.")
        return turn-1

    else:
        print("YOU CHOOSED THE CORRECT NUMBER. YOU WON!!")


def set_difficulty():
    level = input("choose a difficulty. Type 'easy' or 'hard': ")
    if level == "hard":
        return hard_level_turn  # i use return in palce of using global
        # return will let me call the function set_difficulty.

    else:
        return easy_level_turn


def game():
    print("WELCOME TO THE NUMBER GUESSING GAME! ")
    print("I AM THINKING OF A NUMBER BETWEEN 1 AND 100. ")

    random_integer = int(random.randint(1, 100))  # [1,100]
    # print(random_integer)
    turns = set_difficulty()

    guess = 0
    while guess != random_integer:
        print(f"you have {turns} attempts left. ")

        guess = int(input(" guess a number: "))
        turns = check_answer(guess, random_integer, turns)
        if turns == 0:
            print(" you loose. ")
            return


game()
