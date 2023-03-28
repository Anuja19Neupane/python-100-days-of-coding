from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "D:\python-learning\chromedriver.exe "
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.yahoo.com/?guccounter=1")

# to click in sign in
sign_in = driver.find_element_by_css_selector("#ybarAccountProfile")# here # means id
sign_in.click()


# to click in email
email=driver.find_element_by_id("login-username")
email.click()

# to give data in email
give_email=email.send_keys("anujaneupane20@gmail.com")
email.send_keys(Keys.ENTER)

# to tick i am not robot
not_robot=driver.find_element_by_class_name("bucket-mbr-push-upshell-exp2")
not_robot.send_keys(Keys.ENTER)



to click in next



time.sleep(1000)
