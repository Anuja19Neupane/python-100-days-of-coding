# note: to find maximum or minimum value we can directly use max or min function but use for loop here.
scores = [36, 37, 89, 45, 45]
heighest_score = 0
for score in scores:
    if score > heighest_score:
        heighest_score = score
print(heighest_score)
