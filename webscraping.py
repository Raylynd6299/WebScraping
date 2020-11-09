from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://mundofreestyle.com/clasificacion-fms-mexico-tabla-de-posiciones/"
page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")

#Participantes

pt = soup.find_all("td",class_='column-1')
clasificacion =[]
for part in pt:
    clasificacion.append(part.text)

nombres = soup.find_all("td",class_='column-2')
Nombres = []
for nombs in nombres:
    Nombres.append(nombs.text)

score = soup.find_all("td",class_='column-3')
Score = []
for sco in score:
    Score.append(sco.text)

puntos = soup.find_all("td",class_='column-4')
Puntos = []
for pont in puntos:
    Puntos.append(pont.text)
    
df = pd.DataFrame({"Clasificaccion":clasificacion,"Nombre":Nombres,"Score":Score,"Puntos":Puntos})

print(df)