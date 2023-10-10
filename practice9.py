# Write a program that takes a list of strings and returns a new list that contains only the strings that have more than three characters.
words = ["hello", "world", "python", "hi", "a", "cat"]
 
def chosen_word(words):
    
    new_list = []
    for word in words:
        if len(word) > 3:
            new_list.append(word)
    return new_list



filtered_words = chosen_word(words)
print(filtered_words)