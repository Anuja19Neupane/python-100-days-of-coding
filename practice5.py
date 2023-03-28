#Write a program that takes two lists and returns a new list that contains only the common elements between the two lists.

list1 = [45, 26, 3, 48, 5]
list2 = [3, 47, 5, 60, 72]


def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2 and element not in common_elements:
            common_elements.append(element)
    return common_elements



common_elements = find_common_elements(list1, list2)
print(f"The common elements between list1 and list2 are: { str(common_elements)}")