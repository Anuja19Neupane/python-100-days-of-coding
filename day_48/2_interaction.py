from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "D:\python-learning\chromedriver.exe "
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count=driver.find_element_by_css_selector("#articlecount a") # here #means it is id
# print(article_count.text)  

search=driver.find_element_by_name("search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

time.sleep(1000)