# Write a program that takes a string and returns the number of words in the string.


string="anuja is don"


def no_of_word(string):
    words = string.split()
    return len(words)


num_words = no_of_word(string)
print(f" Number of words:{num_words}") 
