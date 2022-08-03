from pathlib import Path
import re, csv

def overheads():
    overheads_list= []
    path = Path.cwd()/'project_group'/'csv_reports'/'Overheads.csv'
    with path.open(mode= "r", encoding= "UTF-8") as file:
        reader= csv.reader(file)
        next (reader)

        for line in reader:
            overheads_list.append(line)
        return overheads_list
        
#print(overheads())

def cash_on_hand():
    coh_list = []
    path = Path.cwd()/'project_group'/'csv_reports'/'cash-on-hand-usd.csv'
    with path.open(mode = "r",encoding="UTF-8",newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for line in reader:
            coh_list.append(line)
        return coh_list

# print(cash_on_hand())

def profit_and_loss():
    pnl_list = []
    path = Path.cwd()/'project_group'/'csv_reports'/'profit-and-loss-usd.csv'
    with path.open(mode = "r",encoding="UTF-8-sig",newline="") as file:
        reader = csv.reader(file)
        
        for line in reader:
            pnl_list.append(line)
        return pnl_list

#print(profit_and_loss())