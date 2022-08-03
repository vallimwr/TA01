from pathlib import Path
import re, csv

overhead_value = []
overhead_list = []

def overheads():
    path = Path.cwd()/'project_group'/'csv_reports'/'Overheads.csv'
    with path.open(mode= "r", encoding= "UTF-8") as file:
        reader= csv.reader(file)
        next(reader)

        for line in reader:
            overhead_value.append(float(line[1]))
            maximum_value = max(overhead_value)
            overhead_list.append(line)
            return f"{maximum_value}"
    
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