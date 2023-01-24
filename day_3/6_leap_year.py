year = int(input("Enter a year "))
remainder = year % 4
if remainder != 0:
    print("NOT LEAP YEAR")
else:

    remainder2 = year % 100
    if remainder2 == 0:
        remainder3 = year % 400
        if remainder3 != 0:
            print("NOT LEAP YEAR")
        else:
            print("LEAP YEAR")

    else:
        print("LEAP YEAR")
