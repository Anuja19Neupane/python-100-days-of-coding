import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

BUY_PRICE = 200
YOUR_EMAIL_1 = "forpython959@gmail.com"
YOUR_PASSWORD = "fC0x7Tgt"
TO_EMAIL = "gibygirl16@gmail.com"

url = "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ?th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

price_element = soup.select_one('.a-price')

price_text = price_element.get_text()
price_without_currency = price_text.replace("$", " ")
price_as_float = float(price_without_currency)

title_element = soup.find("h1")
title = title_element.get_text().strip()

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price_text}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:# 587is default port number
        connection.starttls()
        result = connection.login(YOUR_EMAIL_1, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL_1,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        ) 