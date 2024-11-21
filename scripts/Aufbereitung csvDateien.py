import pandas as pd
import csv
import os

def process_csv(input_file, output_file, error_file, expected_columns, delimiter=';'):
    """
    Diese Funktion liest eine CSV-Datei mit Semikolon-Trennzeichen, passt fehlerhafte Zeilen an oder speichert sie in einer Fehlerdatei.

    Parameters:
        input_file (str): Pfad zur Eingabedatei.
        output_file (str): Pfad zur bereinigten Ausgabedatei.
        error_file (str): Pfad zur Datei mit fehlerhaften Zeilen.
        expected_columns (int): Erwartete Anzahl an Spalten.
        delimiter (str): Trennzeichen der CSV-Datei.
    """
    # Listen für korrekte und fehlerhafte Zeilen
    valid_rows = []
    error_rows = []

    # Header und Zeilen prüfen
    with open(input_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter)  # Semikolon als Trennzeichen
        header = next(reader)  # Header auslesen
        print(f"Gelesener Header: {header}")
        if len(header) != expected_columns:
            raise ValueError(f"Header hat nicht die erwartete Anzahl an Spalten: {len(header)} (erwartet: {expected_columns})")

        for line_number, row in enumerate(reader, start=2):  # Zeilennummer ab 2 (wegen Header)
            if len(row) == expected_columns:
                valid_rows.append(row)
            else:
                # Fehlerhafte Zeilen: Anpassen oder Speichern
                if len(row) > expected_columns:
                    # Zu viele Spalten: Überflüssige abschneiden
                    row = row[:expected_columns]
                    valid_rows.append(row)
                elif len(row) < expected_columns:
                    # Zu wenige Spalten: Fehlende Werte auffüllen
                    row.extend([''] * (expected_columns - len(row)))
                    valid_rows.append(row)
                else:
                    error_rows.append((line_number, row))

    # Bereinigte Daten speichern
    with open(output_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(header)  # Schreibe den Header
        writer.writerows(valid_rows)

    # Fehlerhafte Zeilen speichern
    with open(error_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(["Zeile", "Inhalt"])  # Kopfzeile für Fehlerdatei
        for line_number, row in error_rows:
            writer.writerow([line_number, row])

    print(f"Bereinigung abgeschlossen: {output_file}")
    print(f"Fehlerhafte Zeilen gespeichert in: {error_file}")

# Beispielnutzung
input_file = "data/raw/tbl_Vergleich_GV_GuenstjePostort_2Stichtage_Strom.csv"
output_file = "data/processed/cleaned_file.csv"
error_file = "data/processed/error_lines.csv"
expected_columns = 14  # Erwartete Spaltenanzahl

# Verzeichnis erstellen, falls nicht vorhanden
os.makedirs(os.path.dirname(output_file), exist_ok=True)

process_csv(input_file, output_file, error_file, expected_columns)
