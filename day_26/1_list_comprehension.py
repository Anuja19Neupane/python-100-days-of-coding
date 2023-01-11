

numbers = [1, 2, 3, 4, 5, 6, 7, 8]


# +1
new_list = [n+1 for n in numbers]
print(new_list)


# sqaure
neww_list = [n*n for n in numbers]
print(neww_list)


# print only even
result = [num for num in numbers if num % 2 == 0]
print(result)
