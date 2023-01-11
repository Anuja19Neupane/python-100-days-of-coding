def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    ygdgieyudhusufhkhsgfuhlsijdhhuj


    # return paxi lekheko kura execute hudaina.
    # if written in same block.
    # return le yo function ko end ho vanney kura denote garxa.
print(format_name("anuja", "neupane"))


# input kei diyena user le vaney:
def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return  # input kei navako bela return le none print garxa.
       # user le input nadida hamile kei msg garnuparxa vaney:
       # return"please answer all questions."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name(input("first name: "), input("last name: ")))
