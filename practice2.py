# Write a program that takes a list of numbers and returns a new list that contains only the even numbers from the original list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_even_numbers(original_list):
    even_numbers = []
    for num in original_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

even_numbers = get_even_numbers(original_list)
print(even_numbers) 