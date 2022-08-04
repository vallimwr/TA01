from api import forex
from pathlib import Path
import re, csv

def cash_on_hand():
    coh_list = []
    path = Path.cwd()/'project_group'/'csv_reports'/'cash-on-hand-usd.csv'
    with path.open(mode = "r",encoding="UTF-8",newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for line in reader:
            coh_list.append(line)
        return coh_list

print(cash_on_hand())

import coh

def cashonhand_write():
    list = []
    day = []
    for value in list:
        list.append(float(value[1])*forex)