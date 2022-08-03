from api import forex
from pathlib import Path
import csv

full_list = []
overhead_list = []

file_path = Path.cwd()/'csv_reports'/'Overheads.csv'
with file_path.open(mode= 'r', encoding= 'UTF-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    print (header)
    for line in reader:
        full_list.append(line)