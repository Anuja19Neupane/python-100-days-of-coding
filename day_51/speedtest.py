from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




chrome_driver_path = "D:\python-learning\chromedriver.exe "
driver = webdriver.Chrome(executable_path=chrome_driver_path)

speedtest=driver.get("https://www.speedtest.net/")

go_button = driver.find_element_by_class_name("start-text")
go_button.click()
download=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')

print(download.text)
print("done")




# time.sleep(10000)


driver.quit()
     
