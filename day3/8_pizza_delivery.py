print("WELCOME TO PYTHON PIZZA DELIVERIES.")
size = input("which size pizza do you want? small,medium or large? ")
bill = 0
if size == "small":
    print(f"It's ${bill+5}.")
elif size == "medium":
    print(f"It's ${bill+6}.")
elif size == "large":
    print(f"It's ${bill+7}.")
