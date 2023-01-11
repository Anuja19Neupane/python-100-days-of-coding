weather_c = {
    "monday": 12,
    "tuesday": 13,
    "wednesday": 15,
    "thursday": 17,
    "friday": 15,
    "saturday": 14,
    "sunday": 17
}

weather_f = {day: (tem_c*9/5)+32 for (day, tem_c) in weather_c.items()}
print(weather_f)
