name1 = input("enter your name. ")
name2 = input("enter the other person name. ")
combined_name = name1+name2

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
true = t+r+u+e
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l+o+v+e
love_score = str(true)+str(love)
print(f"your score is {love_score}.")
