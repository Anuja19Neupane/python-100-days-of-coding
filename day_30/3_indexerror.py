fruits = ["apple", "pear", "mango"]


def make_pie(index):
    try:
        fruit = fruits[index]

    except IndexError:
        print("fruit pie")
#  IndexError huda matra fruit pie print huu

    else:
        print(fruit+"pie")


make_pie(4)

# here there is no any fruit name in index 4
# applie in position 0,pear 1,mango 2
