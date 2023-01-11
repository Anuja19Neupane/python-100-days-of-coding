# Selenium is a suite of tools to automate web browsers.
# It allows you to write scripts in various programming languages to automate web browsers and
#  perform tasks such as web scraping,
#  testing web applications, and automating actions on websites.


# mero chrome ko version:Version 108.0.5359.125 (Official Build) (64-bit)

from selenium import webdriver


chrome_driver_path = "D:\python-learning\chromedriver.exe " # chrome driver ko path ho
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

# driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ?th=1")
# price=driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

bug_link=driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


#driver.close()
#yesle specific tab lai matra banda garxa
driver.quit()
#yesle purei browser banda garxa

