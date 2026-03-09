import pandas as pd

df = pd.read_excel("data.xlsx")
df["Si/Al"] = df["Si"] / df["Al"]

print(df)
