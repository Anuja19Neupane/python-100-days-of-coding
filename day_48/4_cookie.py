from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "D:\python-learning\chromedriver.exe "
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
mouse_click=driver.find_element_by_id("cookie")

for i in range(200):
    mouse_click.click()
    time.sleep(0.001)


time.sleep(15)
