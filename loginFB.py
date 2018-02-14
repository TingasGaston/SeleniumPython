from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path=r'C:\Users\Windows 7\Downloads\geckodriver-v0.19.1-win64\geckodriver.exe')
browser.get('https://facebook.com')
time.sleep(10)
#user credentials
user = browser.find_element_by_css_selector('#email')
user.send_keys('gastonarios@yahoo.com.ar')
password = browser.find_element_by_css_selector('#pass')
password.send_keys('Cancu233231685')
login = browser.find_element_by_id('u_0_2')
login.click()
