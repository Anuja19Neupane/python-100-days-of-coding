#Write a program that asks the user for a number and then prints out all the prime numbers up to that number.

number=input("write a number: ")
lower = 0
upper = number

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, int(upper) + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)