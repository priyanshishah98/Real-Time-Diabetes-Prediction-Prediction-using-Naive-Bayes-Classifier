import pandas as pd
import sys
import random

main_df = pd.read_csv("classify1.csv")

print(list(main_df))
for row in main_df.iterrows():
    age = row[1][1]
    weight = row[1][2]
    height = row[1][3]
    haemo = row[1][4]
    bmi = row[1][12]
    fasting = row[1][11]
    label = row[1][13]
    a = f"{label} 1:{age} 2:{haemo} 3:{bmi} 4:{fasting}" +"\n"
    # a = f"({label},[{age},{haemo},{bmi}])" + "\n"
    f = open("predia2.txt","a")
    f.write(a)
    f.close()

