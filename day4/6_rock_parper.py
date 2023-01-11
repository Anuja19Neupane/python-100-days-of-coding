import random
choose = (input("rock,paper or scissor:"))
# print(choose)
if choose == "rock":
    print("you choosed rock")
elif choose == "paper":
    print("you choosed paper")
elif choose == "scissor":
    print("you choosed scissor")
   # import random
random_play = random.randint(0, 2)
# print(f"computer choose {random_play}")
if random_play == 0:
    print("computer choose ROCK")
elif random_play == 1:
    print("computer choose PAPER")
elif random_play == 2:
    print("computer choose SCISSOR")
if choose == "rock" and random_play == 2:
    print("YOU WIN!")
elif choose == "paper" and random_play == 0:
    print("YOU WIN!")
elif choose == "scisssor" and random_play == 1:
    print("YOU WIN!")
elif choose == "rock" and random_play == 1:
    print("YOU LOSE!")
elif choose == "paper" and random_play == 2:
    print("YOU LOSE!")
elif choose == "scissor" and random_play == 0:
    print("YOU LOSE!")
else:  # choose == random_play:
    print("draw")
# else:
  #  print("DRAW")
