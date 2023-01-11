# dictionary is the key value pairs.
dictionary = {"anuja": "neupane", "prashu": "bhandari"}
# anuja is key here and neupane is value
print(dictionary["anuja"])

# create a empty dictionary
empty_dictionary = {}  # just like creating empty list

# wipe an existing dictionary
dictionary = {}
# yesle {} print garxa.this can be useful when hamilai kei kura restart garnu xa.
print(dictionary)

# edit an item in a dictionary
dictionary["anuja"] = "don"
print(dictionary)

# Loop through a dictionary
for key in dictionary:
    print(key)
    print(dictionary)
