import pandas as pd
import csv
import os

DATA = "tbl_Vergleich_GV_GuenstjePostort_2Stichtage_Strom.csv"
ROOT = "https://raw.githubusercontent.com/Takual/Energiepreise/refs/heads/main/data/raw/"


# Importiere die Daten mit europäischem Zahlenformat
df = pd.read_csv(ROOT + DATA, sep=';', decimal=',')
df (head2)
