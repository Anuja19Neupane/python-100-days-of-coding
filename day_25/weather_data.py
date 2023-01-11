# with open("day_25/weather_data.csv") as data:
#  complete_data = data.readlines()
#  print(complete_data)


import csv

with open("day_25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    # reader() is used to read the file, which returns an iterable reader object.
    temperatures = []
    for row in data:
        if row[1] != "temp":  # hamile temp ma vako value matra print garna khojeko in the form of integer
            # but tya temp pani print vayo,so remove gareko
            temperatures.append(int(row[1]))
    print(temperatures)
