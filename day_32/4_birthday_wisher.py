##################### Normal Starting Project ######################

from datetime import datetime
import pandas
import random
import smtplib

my_email="forpython959@gmail.com"
password="epsagwvcmvrdbzou"


# 2. Check if today matches a birthday in the birthdays.csv

today=datetime.now()
today_touple=(today.month,today.day)

data=pandas.read_csv("day_32/birthdays.csv")
birthdays_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}




#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_touple in birthdays_dict:
    birthday_person=birthdays_dict[today_touple]
    # kasko birthday ho vanera thahpauna touple sanga match gareko name hunuparxa
    file_path=f"day_32/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME",birthday_person["name"])
        # NAME vako thau ma birhday person ko name lekhna parxa
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"subject:BIRTHDAY!!\n\n {contents} ")






