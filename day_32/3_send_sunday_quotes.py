import smtplib
import random
import datetime as dt

my_email="forpython959@gmail.com"
password="epsagwvcmvrdbzou"

now=dt.datetime.now()
day_of_week=now.weekday()
if day_of_week==6:
    with open("day_32/quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote=random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject:Today's Motivation\n\n{quote}"
        )