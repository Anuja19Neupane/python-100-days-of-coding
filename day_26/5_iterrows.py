#import pandas
from pandas import DataFrame
students_dict = {"people": [
    "anuja", "abi", "prashu"],
    "score": [56, 67, 45]
}

student_data_frame = DataFrame(students_dict)
# print(student_data_frame)


for (index, row) in student_data_frame.iterrows():
   # print(row)
    # print(type(row))
    print(row.score)
