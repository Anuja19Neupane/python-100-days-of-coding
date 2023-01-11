from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "D:\python-learning\chromedriver.exe "
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://appbrewery.com/p/newsletter")
search=driver.find_element_by_id("member_email")
search.send_keys("anujaneupane20@gmail.com")
search.send_keys(Keys.ENTER)

time.sleep(100)


