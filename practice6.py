# Write a program that takes a sentence and returns a new sentence with all the words in reverse order.

sentence = "bella is now 3 months"


def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))  # 'reversed()' function le sentence lai reverse garxa.
                                            #  so we convert it to a list using the list() function and then pass it to the join() 
                                            # method to join the words back together with a space separator.
    return reversed_sentence



reversed_sentence = reverse_words(sentence)
print(f"The reversed sentence is: { reversed_sentence}")