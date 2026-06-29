import pandas as pd

df = pd.read_csv("NBA_Shots_2021-22.csv")

averages = df.groupby("name")["score_value"].sum()
print(averages)