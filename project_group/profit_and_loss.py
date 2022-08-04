from api import forex
from pathlib import Path
import re, csv

def profit_and_loss():
    pnl_list = []
    path = Path.cwd()/'project_group'/'csv_reports'/'profit-and-loss-usd.csv'
    with path.open(mode = "r",encoding="UTF-8-sig",newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for line in reader:
            pnl_list.append(line)
        return pnl_list
        
print(profit_and_loss())
import profit_and_loss

def pnl_write(): 
    all_pnl= []
    #A= profit_and_loss()
    for value in profit_and_loss():
        all_pnl.append(value)
    print(all_pnl)

    
    # for larger_fig in all_pnl[4]:
    #     if larger_fig:
            #print(larger_fig)

    #print(data)

#profit_and_loss_write()