import pandas as pd
import os

# Pfade zu den Rohdaten und den Verarbeiteten Dateien
raw_path = "/mnt/data/raw"
processed_path = "/mnt/data/processed/"

# Sicherstellen, dass der Ausgabeordner existiert
os.makedirs(processed_path, exist_ok=True)

# Dateien, die verarbeitet werden sollen
files = [
    "tbl_Vergleich_GV_GuenstjePostort_2Stichtage_Gas.csv",
    "tbl_Vergleich_GV_GuenstjePostort_2Stichtage_Strom.csv",
]

# Funktion zur Bereinigung und Verarbeitung
def clean_and_process_file(input_file, output_file):
    try:
        # Versuche die Datei mit verschiedenen Trennzeichen zu laden
        df = None
        for delimiter in [',', ';', '\t']:
            try:
                df = pd.read_csv(input_file, delimiter=delimiter)
                break
            except Exception:
                continue

        if df is None:
            raise ValueError(f"Datei konnte nicht geladen werden: {input_file}")

        # Entfernen von leeren Zeilen
        df.dropna(how='all', inplace=True)

        # Überprüfen auf doppelte Einträge und Entfernen
        df.drop_duplicates(inplace=True)

        # Optional: Weitere spezifische Bereinigungen durchführen
        # (Anpassungen können nach Bedarf erfolgen)

        # Bereinigte Datei speichern
        df.to_csv(output_file, index=False)
        print(f"Datei erfolgreich verarbeitet und gespeichert: {output_file}")
    except Exception as e:
        print(f"Fehler bei der Verarbeitung der Datei {input_file}: {e}")

# Verarbeitung der Dateien
for file in files:
    input_file = os.path.join(raw_path, file)
    output_file = os.path.join(processed_path, file)
    clean_and_process_file(input_file, output_file)