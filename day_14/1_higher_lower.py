# problem solved
# right garda score 1 aauxa wrong garda 0. but i want it to increase if right and stop if wrong.

import random
print("WELCOME TO HIGHER_LOWER GAME.")
print("WHO HAS MORE FOLLOWERS IN INSTAGRAM?")

celebritiy = {"ronaldo": 508,
              "ariana": 342,
              "Virat Kohli": 225,
              "shakira": 77,
              "zendaya": 159,
              "justin": 267,
              "kylie": 373,
              "taylor": 243,
              "kim": 334,
              "billie": 107,
              "messi": 386,
              "neymar": 191,
              "selena": 362,
              "kendall": 265,
              "gigi": 76,
              "bella": 56,
              "zayn": 47,
              "harry": 48,
              "dua": 87,
              "camilla": 65,
              "sawm_mandes": 71,
              "tom_holland": 67,
              "katy_perry": 182,
              "instagram_official": 575,
              "millie_bobby": 60,
              "mr.beast": 21,

              "priyanka_chopra": 83
              }


# random.sample() use garda different item choosehunxa list bata.
# random_celebrity_1, random_celebrity_2 = random.sample(celebritiy.keys(), 2)
# we can also use:
# if random_celebrity_1==random_celebrity_2:
#   random_celebrity_1=random.choice(list)


def check_guess(random_celebrity_1, random_celebrity_2, guess):
    if celebritiy[random_celebrity_1] > celebritiy[random_celebrity_2] and guess == 1:
        correct = True
        return correct

    elif celebritiy[random_celebrity_1] > celebritiy[random_celebrity_2] and guess == 2:
        correct = False
        return correct

    elif celebritiy[random_celebrity_1] < celebritiy[random_celebrity_2] and guess == 1:
        correct = False
        return correct
    elif celebritiy[random_celebrity_1] < celebritiy[random_celebrity_2] and guess == 2:
        correct = True
        return correct


guesss_right = True
score = 0

while guesss_right:
    random_celebrity_1, random_celebrity_2 = random.sample(
        celebritiy.keys(), 2)

    guess = int(
        input(f"{random_celebrity_1} OR {random_celebrity_2}? 1 or 2? "))

    if check_guess(random_celebrity_1, random_celebrity_2, guess) == True:
        score += 1
    else:
        guesss_right = False

    print(f"score: {score}")

    # if guess == 1:
    #    score = print(" NOOO!!! ")
    # elif guess == 2:
    #   score = print("YESSS!!!")
    # if score == "NOOO!!!":
    #   print("SORRY, YOU LOOSE. ")
