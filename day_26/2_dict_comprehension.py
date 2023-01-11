# error
# error
# error
# error
# error
# error
# error
# error
# error
# error
# error
# error

# syntax
# new_dict={new_key:new_value for (key,value) in dict.items()}


import random
names = ["anu", "abi", "vai", "prashu"]

students_score = {student: random.randint(1, 100) for student in names}
print(students_score)


passed_students = {student: score for (
    student, score) in students_score.items() if score >= 60}
print(passed_students)
