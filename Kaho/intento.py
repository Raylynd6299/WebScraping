from selenium.webdriver.common.keys import Keys
from selenium.webdriver.opera.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time  

#opciones
options = Options()
options.add_argument("--remote-debugging-port=9222")
#options.add_argument("--headless")
opera_driver = webdriver.Opera(executable_path="operadriver",options=options)

opera_driver.get("https://kahoot.it/challenge/09168452?challenge-id=3882dbfd-4f85-4e86-9fa2-018882d19a9a_1605679445775")

delay  = 20

nickname = "RaymundoPulido"
user = None
try:
    user = WebDriverWait(opera_driver,delay).until(EC.presence_of_element_located((By.ID,"nickname")))
except TimeoutException:
    print("Error al abrir el inicio de Seccion")
    
if user != None:
    time.sleep(1)
    user.click()
    user.send_keys(nickname)
    submit = opera_driver.find_element_by_xpath("//button[@data-functional-selector='join-button-username']")
    submit.click()
    
lista = []

try:
    opciones = WebDriverWait(opera_driver,delay).until(EC.presence_of_all_elements_located((By.XPATH,"//div[@data-mapped-index]")))
except Exception as e:
    pass