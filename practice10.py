# Write a program that takes a list of numbers and returns the sum of the squares of those numbers.

numbers = [1, 5, 6, 22, 11]


def sum_squares(numbers):
    new_list = []
    for num in numbers:
        new_list.append(num**2)
    return sum(new_list)



sum_of_squares = sum_squares(numbers)
print(f"sum_of_squares is: {sum_of_squares}")