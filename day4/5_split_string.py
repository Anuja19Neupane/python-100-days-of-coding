import random
number = int(input("enter the total number of people. "))
names = input("give me all the names(please separate it by comma). ")
list = names.split(",")
print(list)
int(len(list))
random_integer = random.randint(0, number-1)
print(random_integer)
one_who_should_pay = list[random_integer]
print(one_who_should_pay + " should pay the bill. ")
# if random_integer == 0:
#print("person 1 have to pay the bill.")
# elif random_integer == 1:
#   print("person 2 have to pay bill")
# elif random_integer == 2:
#   print("person 3 have to pay bill")
# elif random_integer == 3:
#   print("person 4 have to pay bill")
