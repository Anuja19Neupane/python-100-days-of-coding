from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "D:\python-learning\chromedriver.exe "
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.instagram.com/")

#click to input phonenumber
phone_number=driver.find_element_by_id("splash-screen")


# give phonenumber
give_number=phone_number.send_keys("9829322128")
phone_number.send_keys(Keys.ENTER)



# #click to input password
# password=driver.find_element_by_class_name


time.sleep(100)

