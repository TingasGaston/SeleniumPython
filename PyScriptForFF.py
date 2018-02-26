from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r'C:\Users\Windows 7\Downloads\geckodriver-v0.19.1-win64\geckodriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://www.google.com.ar")

searchField = driver.find_element_by_id("lst-ib")
searchField.clear()

searchField.send_keys("Selenium WebDriver Interview questions")
searchField.submit()

lists = driver.find_element_by_class_name("_Rm")

#print("Found " + str(len(lists)) + "searches: ")
i = 0
for listitem in lists:
    print(listitem)
    i = i + 1
    if i > 10:
        break
driver.quit()
