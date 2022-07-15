from bs4 import BeautifulSoup
import requests
import time
import csv
import pandas as pd

uri = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
#browser = webdriver.Chrome("/Users/omgautam/Desktop/Project127/venv/chromedriver")
#browser.get(uri)
time.sleep(10)
page = requests.get(uri)

soup=BeautifulSoup(page.text,"html.parser")
start_table = soup.find('table')
temp_list = []
table_row = start_table.find_all("tr")
for tr in table_row:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_name = []
distance = []
mass = []
radius = []

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df = pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns = ['star_name','distance','mass','radius'])
print(df)
df.to_csv('bright.csv')




