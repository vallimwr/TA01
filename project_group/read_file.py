from api import forex
from pathlib import Path
import re, csv

def overheads():
    overhead_value = []
    overhead_list = []
    path = Path.cwd()/'project_group'/'csv_reports'/'Overheads.csv'
    with path.open(mode= "r", encoding= "UTF-8") as file:
        reader= csv.reader(file)
        next(reader)

        for value in reader:
            overhead_value.append(float(value[1]))
            overhead_list.append(value)
            return f"{max(overhead_value)}"
    
print(overheads())

blank_list = []

def cash_on_hand():
     path = Path.cwd()/'project_group'/'csv_reports'/'cash-on-hand-usd.csv'
     with path.open(mode = "r",encoding="UTF-8",newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for line in reader:
            for value in line:
                blank_list.append(float(value))

            print(blank_list)