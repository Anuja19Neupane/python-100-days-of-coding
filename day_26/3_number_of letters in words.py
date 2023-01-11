sentence = "who is anuja?"

# for word in sentence.split():
#   print(word)

result = {word: len(word) for word in sentence.split()}
print(result)
