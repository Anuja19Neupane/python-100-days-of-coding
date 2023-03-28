# note:this can be done without foor loop also but we are learning to use foor loop so use it.
student_height = [123, 152, 132, 161, 135]
total_height = 0
for height in student_height:
    total_height += height
print(f"total height is: {total_height}.")
number_of_people = 0
for student in student_height:
    # number_of_people 0 dekhi suru xa so loop ek palta besi run hunuparxa ie.number_of_people = 4 xa vaney there are altogethe 5 people so loop should run 5 times.
    number_of_people += 1
average_height = total_height/number_of_people
print(f"average height is: {average_height}.")
