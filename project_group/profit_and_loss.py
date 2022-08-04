#from api import forex
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
   
#print(profit_and_loss())

def pnl_write(): 
    all_pnl= []
    pnl_days= []
    for value in profit_and_loss():
        all_pnl.append(float(value[4]))
    print(all_pnl)

    for days in profit_and_loss():
        pnl_days.append(days[0])
    print(pnl_days)

    if all_pnl[0]> all_pnl[1]:
        deficit_amount= all_pnl[0]- all_pnl[1]
    print(deficit_amount)
        

    # for larger_fig in all_pnl[4]:
    #     if larger_fig:
    #         print(larger_fig)

pnl_write()