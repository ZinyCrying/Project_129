from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(5)

page = requests.get(START_URL)

soup = BeautifulSoup(page.content, "html.parser")

tables = soup.find_all("table", attrs=["class", "wikitable sortable"])
    #print(table)

    #print(len(tables))

row_list = []

#this is table 1 class = wikitable sortable
#print(tr_tags)
#this is table 2 class = Field brown dwarfs
table_rows = tables[2].find_all('tr')

#print(table_rows)
for each_row in table_rows:
    td_tags = each_row.find_all('td')
    row = [i.text.strip() for i in td_tags]
    row_list.append(row)

Star_names = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(row_list)):
    Star_names.append(row_list[i][0])
    Distance.append(row_list[i][5])
    Mass.append(row_list[i][7])
    Radius.append(row_list[i][8])

#print(brown_dwarfs)

#data_of_df_2 = df.iloc[:,[0,5,7,8]]  

headers = ["Star Name", "Distance", "Mass", "Radius"]

df_1 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=headers)

print(df_1)

df_1.to_csv("scraped_data_2.csv", index=True, index_label="id" )    
    
