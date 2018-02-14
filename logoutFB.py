from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#from selenium folder include webdriver folders

driver = webdriver.Firefox(executable_path=r'C:\Users\Windows 7\Downloads\geckodriver-v0.19.1-win64\geckodriver.exe')
#Using this, we create the Firefox instance of Selenium webdriver.
driver.maximize_window()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
user = driver.find_element_by_id("email")
user.clear()
user.send_keys("gastonarios@yahoo.com.ar")

passw = driver.find_element_by_id("pass")
passw.clear()
passw.send_keys("cancu233231685")

passw.send_keys(Keys.RETURN)

time.sleep(10)
logout = driver.find_element_by_id("userNavigationLabel")
logout.click()
logout1 = driver.find_element_by_css_selector("._w0d[action='https://www.facebook.com/logout.php?button_name=logout&button_location=settings']").submit()
logout1.click()

time.sleep(5)

#driver.quit()




