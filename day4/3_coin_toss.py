import random
toss = input("type 'toss' to toss the coin. ")
random_int = random.randint(1, 2)
if random_int == 1:
    print("head")
else:
    print("tail")
