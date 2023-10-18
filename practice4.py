#Write a program that takes a list of words and returns the longest word in the list.


word_list = ["cat", "dog", "elephant", "bella", "giraffe"]
def find_longest_word(words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word



longest_word = find_longest_word(word_list)# function call
print(f"The longest word in the list is: {longest_word}")