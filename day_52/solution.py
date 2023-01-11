
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "D:\python-learning\chromedriver.exe "


driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://www.instagram.com/accounts/login/")

# Wait for the phone number input field to be visible
phone_number_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "username"))
)

# Clear the input field and enter the phone number
phone_number_input.clear()
phone_number_input.send_keys("9829322128")

# Find the password input field and enter the password
password_input = driver.find_element_by_name("password")
password_input.clear()
password_input.send_keys("DL2TeLgb5y.WLCK")

# Find the login button and click it
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

# Wait for the page to load
WebDriverWait(driver, 10).until(EC.title_contains("Instagram"))

# Print the page title to confirm that the login was successful
print(driver.title)

time.sleep(20)
# Don't forget to close the browser when you're done
driver.close()