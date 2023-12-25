import os
import csv

def save_as_csv(file_name, object, headers):
    file_exists = os.path.isfile(file_name)
    with open(file_name, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(object.to_csv_row())
