import pandas

data = pandas.read_csv("day_25/weather_data.csv")
print(data["tem"])


# dictionary

data_dict = data.to_dict()  # converts to dictianary
print(data_dict)

temp_list = data["tem"].to_list()
print(temp_list)

average = int(sum(temp_list)/len(temp_list))
print(f"the average temperature is {average}.")


# here data["tem"] is series,series is like list of day to day life
print(data["tem"].mean())
max_temp = print(data["tem"].max())


# get data in columns
print(data["conidtion"])
print(data.conidtion)  # yo duitei le exact same kaam garxa


# get data in rows
data[data["day"] == "monday"]
print(data[data.day == "monday"])  # yo duitei le exact same kaam garxa

print(data[data.tem == data["tem"].max()])


# monday ko temper lai farhenhheit ma convert garney

monday = data[data.day == "monday"]
monday_temp = int(monday.tem)
monday_temp_f = (monday_temp*9/5)+32
print(monday_temp_f)

# create a dataframe from scratch

data_dict = {
    "name": ["anu", "abi"],
    "score": [20, 25]

}
data = pandas.DataFrame(data_dict)
print(data)

# mathi dictionary ma vako kura lai dataframe ma arkei file ma rakhna

data_dict = {
    "name": ["anu", "abi"],
    "score": [20, 25]

}
data = pandas.DataFrame(data_dict)
data.to_csv("day_25/testing.csv")
