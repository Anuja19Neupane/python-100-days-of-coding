height = float(input("enter your height in meter. "))
weight = int(input("enter your weight in kg. "))
bmi = weight/height ** 2
if bmi <= 20:
    print("SLIM")
elif bmi <= 24:
    print("IDEAL WEIGHT")
elif bmi <= 28:
    print("OVERWEIGHT")
elif bmi > 28:
    print("OBESE")
