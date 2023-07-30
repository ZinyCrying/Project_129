import pandas as pd
import csv

rows = []

with open("./scraped_data_2.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

#print(rows)

headers = rows[0]
body = rows[1:]

#print("headers: \n", headers) 

temp_list = list(body)

for star_data in temp_list:
    star_mass = star_data[3]
    if star_mass == '':
        temp_list.remove(star_data)
#print(len(temp_list))
        continue
    else:
        star_mass_value = float(star_data[3]) * 0.000954588
        star_data[3] = star_mass_value

#print(temp_list)

for str_radius in temp_list:
    star_radius = str_radius[4]
    if star_radius == '':
        temp_list.remove(str_radius)
        continue
#print(len(temp_list))
    else:
        star_radius_value = float(str_radius[4]) * 0.102763
        str_radius[4] = star_radius_value

print(len(temp_list))
column1 = ["Star Name", "Distance", "Mass", "Radius"]

df_1 = pd.DataFrame(temp_list, columns=column1)
df_1.to_csv("scraped_data_3.csv")

column2 = ["Star Name", "Distance", "Mass", "Radius", "Luminosity"]

#df_2 = pd.DataFrame(columns=column2)
#df_2 = pd.merge("scraped_data_2.csv", "scraped_data_3.csv")

#df_2.to_csv("final_scraped_data.csv", index=True, index_label="id")




