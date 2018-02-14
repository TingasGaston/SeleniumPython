from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\Users\Windows 7\Downloads\geckodriver-v0.19.1-win64\geckodriver.exe')
browser.get('http://seleniumhq.org/')
