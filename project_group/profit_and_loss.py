#from api import forex
from pathlib import Path
import re, csv

def profit_and_loss():
    pnl_list = []
    path = Path.cwd()/'project_group'/'csv_reports'/'profit-and-loss-usd.csv'
    with path.open(mode = "r",encoding="UTF-8-sig",newline="") as file:
        reader = csv.reader(file)
        
        for line in reader:
            pnl_list.append(line)
        return pnl_list
        
profit_and_loss()

def profit_and_loss_write(): 
    all_pnl= []
    A= profit_and_loss()
    for data in A:
        all_pnl.append(data)

    print(data)

profit_and_loss_write()