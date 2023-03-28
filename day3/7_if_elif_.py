bill = int(input("what is your previous bill? $"))
# print(bill)
photo = input("Do you want photo to be printed? ")
if photo == "no":  # note:'no' and 'No' are different here.
    print(f"your total bill is {bill}")
else:
    print(f"your total bill is {bill+3} . ")
