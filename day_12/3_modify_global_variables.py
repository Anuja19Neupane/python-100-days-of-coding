enemies = 1


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies+1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# next example

a = 10  # it is global variable


def sth():
    global a
    a = 15  # it is local variable
    # if i want my local variable to be global variable(i.e  a=15 to be my global variable then i use useglobal function as above)
    # it will replace outside with 15.
    print(f"inside: {a}")


sth()
print(f"outside: {a}")
