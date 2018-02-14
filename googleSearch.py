import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Windows 7\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("http://www.google.com")
assert "Google" in driver.title
textbox = driver.find_element_by_name("q")
textbox.send_keys("python")
time.sleep(5)
button = driver.find_element_by_name("btnK")
button.click()
time.sleep(5)
driver.close()