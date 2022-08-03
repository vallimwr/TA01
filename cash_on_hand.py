# from api import forex
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

import cash_on_hand
list = cash_on_hand()

def cashonhand_write():
    list = []
    for value in list:
        list.append(value[1])
    return list

    





