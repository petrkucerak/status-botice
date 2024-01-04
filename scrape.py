import requests
from bs4 import BeautifulSoup
import re
import csv
from datetime import date

CLEANR = re.compile('<.*?>')
URL = 'https://hydro.chmi.cz/hppsoldv/popup_hpps_prfdyn.php?seq=37816755'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.findAll('table', {'style': 'width:100%;'})[1]

data = table.find_all('tr')
for i in range(len(data)):
   if i == 0:
      data[0] = data[0].find_all('th')
      for j in range(len(data[0])):
         data[0][j] = data[0][j].text
      continue
   
   data[i] = data[i].find_all('td')
   for j in range(len(data[i])):
      data[i][j] = data[i][j].text

filename = "data/" + date.today().strftime('%Y-%m-%d') + ".csv"

with open(filename, 'w', newline='') as csvfile:
   w = csv.writer(csvfile, delimiter=',')
   for row in data:
      w.writerow(row)
