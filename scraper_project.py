
from bs4 import BeautifulSoup
from selenium import webdriver

import pandas as pd
import time 

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(5)

scraped_data = []

def scrape():
    
    soup = BeautifulSoup(browser.page_source, "html.parser")

    table = soup.find("table", attrs=["class", "wikitable"])

    table_body = table.find('tbody')

    table_rows = table_body.find_all('tr')
    #print(table_rows)

    for rows in table_rows:
        tb_cols = rows.find_all('td')
        #print("table columns: ", tb_cols)

        temp_list = []

        for cols in tb_cols:
            #print(cols.text)
            data = cols.text.strip()
            #print(data)
            temp_list.append(data)

        scraped_data.append(temp_list)

scrape()

stars_data = []

for i in range(0, len(scraped_data)):

    stars_name = scraped_data[i][1]
    distance = scraped_data[i][3]
    mass = scraped_data[i][5]
    radius = scraped_data[i][6]
    lum = scraped_data[i][7]

    req_data = [stars_name, distance, mass, radius, lum]
    stars_data.append(req_data)

print(stars_data)


headers = ["Star Name", "Distance", "Mass", "Radius", "Luminosity"]

star_df_1 = pd.DataFrame(stars_data, columns=headers)
star_df_1.to_csv("scraped_data.csv", index=True, index_label="id")
        
