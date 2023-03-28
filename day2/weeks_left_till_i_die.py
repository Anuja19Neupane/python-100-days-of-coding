age = input("what is your current age ")
# print(age)
remaining_age = 90-int(age)
print("the remaining age=", remaining_age)
remaining_weeks = remaining_age*52
remaining_months = remaining_age*12
remaining_days = remaining_age*3651
print(
    f"you have {remaining_days} days,{remaining_weeks} weeks,{remaining_months} months left")
