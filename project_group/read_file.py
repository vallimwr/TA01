from pathlib import Path
import re, csv

def overheads():
    path = Path.cwd()/'project_group'/'csv_reports'/'Overheads.csv'
    with path.open(mode= "r", encoding= "UTF-8") as file:
        reader= csv.reader(file)
        next (reader)
        for line in reader:
            print(line)
        
print(overheads())

def cash_on_hand():
    blank_list = []
    path = Path.cwd()/'project_group'/'csv_reports'/'cash-on-hand-usd.csv'
    with path.open(mode = "r",encoding="UTF-8",newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            blank_list.append(line)
            print(line)

print(cash_on_hand())

def profit_and_loss():
    pnl_list = []
    path = Path.cwd()/'project_group'/'csv_reports'/'profit-and-loss-usd.csv'
    with path.open(mode = "r",encoding="UTF-8",newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            pnl_list.append(line)
            print(line)

print(profit_and_loss())