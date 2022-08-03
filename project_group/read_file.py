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
            overhead_list.append(line)
            maximum_value = max(overhead_value)
            return f"{maximum_value}"
    
print(overheads())