import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.opera.options import Options
from selenium import webdriver
import time

options = Options()
options.add_argument("--remote-debugging-port=9222")
#options.add_argument("--headless")

opera_driver = webdriver.Opera(executable_path="operadriver",options=options)  
opera_driver.get("https://www.overleaf.com/login")

usuario = opera_driver.find_element_by_name("email")
usuario.send_keys("rayescomed@gmail.com")

password = opera_driver.find_element_by_name("password")
password.send_keys("cocacola09")

time.sleep(2)
password.send_keys(Keys.ENTER)


time.sleep(2)

driver = opera_driver

driver.execute_script("window.open('');")
time.sleep(2)

driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.google.com")

time.sleep(2)

driver.execute_script("window.open('');")
time.sleep(2)

driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.youtube.com/watch?v=Z8jhFLpk_S4&list=PLf750TN7KFBmDsl4bpx5s_eepsNARd3Lm&index=3")
time.sleep(2)

driver.switch_to.window(driver.window_handles[1])

driver.close()