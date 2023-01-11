# firstly, create dictionary.

MENU = {

    "expresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 65,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 110,
    },
    "cappucino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 110,
    },
}
profit = 0
# hami sanga kati resource available xa?
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}


def is_recource_sufficient(order_ingredients):
    """returns true when order can be made and false if ingredients are insufficient. """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item }. ")
            return False
    return True


def process_coins():
    """returns the total calculated from coins inserted."""
    print("please insert coins. ")
    total = int(input("how many coins of Rs.100? ")*100)
    total += int(input("how many coins of Rs.50? ")*50)
    total += int(input("how many coins of Rs.10? "*10))
    total += int(input("how many coins of Rs.5? ")*5)
    return total


print("WELCOME TO GIBY CAFE.")
print("type 100 to see the report. ")


def is_transaction_sucessful(money_received, drink_cost):
    """returns True when the payment is accepted,or false if money is insufficient. """
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"here is Rs.{change} in change. ")
        # global profit kina leko vaney, profit is defined as global variable but we are using it now in locaal variable.
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough monaey. Money refunded.")
        return False


is_transaction_sucessful(money_received=0, drink_cost=0)


def make_coffee(drink_name, order_ingredients):
    """decrease the required ingrediennts from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}. en joy your day")


is_on = True
while is_on:
    choice = (int(input("expresso,latte,cappucino? 1 or 2 or 3? ")))
    if choice != 1 or 2 or 3:
        is_on = False
    elif choice == 100:
        print(f"water:{resources['water']}ml. ")
        print(f"milk:{resources['milk']}ml. ")
        print(f"coffee:{resources['coffee']}gm. ")
        print(f"money: Rs.{profit}. ")
    else:
        drink = MENU[choice]
        if is_recource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_sucessful(payment, drink["cost "]):
                make_coffee(choice, drink["ingredints"])
