def prime_checker(number):
    number = int(input("enter a number: "))
    is_prime = True
    for i in range(2, number):
        # number=5
        # 5/2
        # 5/3
        # 5/4

        if number % i == 0:
            is_prime = False
    if is_prime:
        print("PRIME")
    else:
        print("NOT PRIME")


prime_checker(number=0)
