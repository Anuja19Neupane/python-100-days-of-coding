fruits = ["apple", "mango", "cherry"]
# if i wrote -1 in place of 1 i will get return from the back ie.cherry.
print(fruits[1])
# if i havae to write orange in place of mango then:
fruits[1] = "orange"
print(fruits)
# to add another fruit:
fruits.append("kiwi")
print(fruits)
# to add something in a list ie.more than 1.
fruits.extend(["lily", "lotus", "rose"])
print(fruits)
