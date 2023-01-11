height=float(input("height: "))
weight=float(input("weight: "))
  


  # user le 3meter vanda badi height nahlos vanera
if height>3:
    raise ValueError

bmi=weight/height **2
print(bmi)