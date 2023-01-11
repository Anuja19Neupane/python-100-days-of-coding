# create an empty dictionary first
students_grades = {}  # empty_dictionary={}
student_scores = {
    "will": 71,
    "mike": 70,
    "dustin": 73,
    "lucas": 72
}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        students_grades[student] = "outstanding"
    elif score > 80:
        students_grades[student] = "excellent"
    elif score > 70:
        students_grades[student] = "very good"
    else:
        students_grades[student] = "YOU TRIED BUT SORRY"
print(students_grades)
