#Write a program that takes a list of numbers and returns the second largest number in the list.

number_list = [32, 37, 51,68, 48, 57, 99, 200]


def find_second_largest(numbers):
    largest = numbers[0]
    second_largest = float(0)
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest



second_largest = find_second_largest(number_list)
print("The second largest number in the list is: " + str(second_largest))