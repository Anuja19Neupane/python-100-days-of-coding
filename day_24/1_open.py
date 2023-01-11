# with open("day_24/test.txt") as file: # file ko thau ma j pani lekhna sakinxa
#    contents = file.read()
#   print(contents)


with open("day_24/test.txt", mode="a") as file:  # a vaneko append
    # day_24/test.txt , yaha vako ma New text.thapinxa
    file.write("\nNew text.")
