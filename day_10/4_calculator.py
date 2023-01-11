# silly mistake
f_number = int(input("What is the first number? "))
print("-")
print("+")
print("/")
print("*")
operation = print(input("Choose an operation: "))
l_number = (int(input("What is the last number? ")))
if operation == "+":
    sum = f_number+l_number
    print(f"sum is {sum}.")
elif operation == "-":
    diff = f_number-l_number
    print(f"dIfference is {diff}. ")
elif operation == "/":
    div = f_number/l_number
    print(div)
elif operation == "*":
    prod = f_number*l_number
    print(prod)
