import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Windows 7\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get("http://www.afar.org.ar/admin.php")
#assert "AFAR -  Asociación de Futbol Amateur Rosario - Menú de Administración" in driver.title
user = driver.find_element_by_name("aid")
user.send_keys("gaston")
time.sleep(5)
password = driver.find_element_by_name("pwd")
password.send_keys("Noelia2010")
time.sleep(5)
button = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[4]/table[2]/tbody/tr/td/table/tbody/tr/td/form/table/tbody/tr[3]/td/input[3]")
button.click()
time.sleep(5)

cargarDatos = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr/td/span[@class='content']/div[1]/strong/strong/a")
cargarDatos.click()

#cargar partidos:

cargarPartidos = driver.find_element_by_xpath("/html/body/table[4]/tbody/tr/td[4]/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[1]/a")
cargarPartidos.click()



#driver.close()