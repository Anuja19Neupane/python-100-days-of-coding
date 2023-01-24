import random
print("WELCOME TO THE PASSWORD GENERATOR")
n_letters = int(input("how many letters would you like in your password? "))
print(n_letters)
n_symbols = int(input("how many symbols would you like? "))
print(n_symbols)
n_numbers = int(input("how many numbers would you like? "))
print(n_numbers)
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '_', '+', '|', '}', '{', ':', ';'',', '<', '>', '?', '.', ]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# easy level
# fgih%*56

# hard level
# f6%ty8$t

# first, easy level

password = ""
# number of letters=4
for char in range(1, n_letters+1):
    password += random.choice(letters)
    # 1,2,3,4
for char in range(1, n_symbols+1):
    password += random.choice(symbols)
for char in range(1, n_numbers+1):
    password += random.choice(numbers)
    random_letter = random.choice(letters)
    # print(random_letter)
    random_symbols = random.choice(symbols)
    # print(random_symbols)
    random_numbers = random.choice(numbers)
    # print(random_numbers)
print(f"password is {password}")
# kina doible time password print vako i dont know.

# hard level

password_list = []
for char in range(1, n_letters+1):
    password_list.append(random.choice(letters))
    # 1,2,3,4
for char in range(1, n_symbols+1):
    password_list.append(random.choice(symbols))
for char in range(1, n_numbers+1):
    password_list.append(random.choice(numbers))
    random_letter = random.choice(letters)
    # print(random_letter)
    random_symbols = random.choice(symbols)
    # print(random_symbols)
    random_numbers = random.choice(numbers)
    # print(random_numbers)
# print(password_list)
random.shuffle(password_list)
#print(f"password is {password_list}")
password2 = ""
for char in password_list:
    password2 += char
print(f"password is {password2}")
