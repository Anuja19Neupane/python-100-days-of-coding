# Write a program that takes a list of strings and returns a new list that contains only the strings that have more than three characters.


def chosen_word(words):
    
    new_list = []
    for word in words:
        if len(word) > 3:
            new_list.append(word)
    return new_list

# Example usage
words = ["hello", "world", "python", "hi", "a", "cat"]
filtered_words = chosen_word(words)
print(filtered_words)