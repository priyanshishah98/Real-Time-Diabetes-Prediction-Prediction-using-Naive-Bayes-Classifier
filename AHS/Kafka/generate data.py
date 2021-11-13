import pandas as pd
import sys

main_df = pd.read_csv("classify2.csv")

print(list(main_df))
for row in main_df.iterrows():
    print(type(row))
    weight = row[1][2]
    height = row[1][3]
    age = row[1][1]
    haemo = row[1][4]
    bmi = row[1][12]
    label = row[1][13]
    # a = f"({label},[{weight},{height},{age},{haemo},{bmi}])" + "\n"
    # a = f"{label }"
    # f = open("../training/traininggggg.txt","a")
    # f.write(a)
    # f.close()

