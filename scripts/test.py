import pandas as pd
import csv
import os

url = "https://raw.githubusercontent.com/Takual/Energiepreise/refs/heads/main/data/raw/tbl_Vergleich_GV_GuenstjePostort_2Stichtage_Strom.csv"
data = pd.read_csv(url, delimiter=';')
data.head(10)
