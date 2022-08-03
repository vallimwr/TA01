from pathlib import Path
import re, csv

overhead_list = []

def overheads():
    path = Path.cwd()/'project_group'/'csv_reports'/'Overheads.csv'
    with path.open(mode= "r", encoding= "UTF-8") as file:
        reader= csv.reader(file)
        next(reader)
        for line in reader:
            overhead_list.append([line])


print(overhead_list)