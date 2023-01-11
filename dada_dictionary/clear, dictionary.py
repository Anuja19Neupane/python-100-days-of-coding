import os
car1 = {
    "name": "porsche",
    "wheel": {"model": 33, "weight": 1},
    "parts": ["seat", "stearing"]
}

# print weight of wheel of car1
print(car1["wheel"]["weight"])
car2 = {
    "name": "audi",
    "wheel": 4,
    "parts": ["seat", "glass"]
}

all_cars = [car1, car2]

# nested for loop
for car in all_cars:
    for key, value in car.items():
        print(key, ":", value)

# print(car1["name"])
# print(car2["name"])

# car1["name"]="TATA"
# print(car1["name"])

# print(len(car1)) #no of key value pair

# print(car1["jpt"]) #key error


for key in car1:  # using looop in simple dict gives keys in the loop
    print(key)

for value in car1.values():  # if we want to iterate over values
    print(value)

for key, value in car1.items():  # each item in the loop is tuple of key and value
    print(key, ":", value)


# dict also behaves as reference
car3 = car1

car3["name"] = "Aayush"  # car1 is also changed


a = int(5)
d = dict(name="myname", caste="Neupane")
d = {"name": "myname", "caste": "Neupane"}


os.system('cls' if os.name == 'nt' else 'clear')
