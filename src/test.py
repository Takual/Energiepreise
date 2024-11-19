import pandas as pd

df = pd.read_csv("https://vscode.dev/github/Takual/Energiepreise/blob/main/data/raw/tbl_Vergleich_GV_GuenstjePostort_2Stichtage_Strom.csv")
print(df.head(10))
