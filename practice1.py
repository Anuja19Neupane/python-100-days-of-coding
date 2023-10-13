# write a program that ask the user for a string and then prints out the number of vowels in the string.

word=input("Write a word: ") 
count=0
#vowel='a','e','i','o','u'

for char in word:
    # word ma vowel xa vaney ,count ma add garney
    if char in "aeiouAEIOU":
        count+=1

print(f"Number of vowels: {count}")