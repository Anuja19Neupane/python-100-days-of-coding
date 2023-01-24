from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "D:\python-learning\chromedriver.exe "
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/app/recs")
# log_in=driver.find_element_by_class_name("M(0) Pos(f)")
# log_in.click()



time.sleep(99999)