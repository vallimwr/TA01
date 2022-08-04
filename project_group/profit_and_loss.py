#from api import forex
from pathlib import Path
import re, csv

file_path = Path.cwd()/'project_group'/'overall_report.txt'
file_path.touch()

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
    for value in profit_and_loss():
        all_pnl.append(float(value[4]))
    print(all_pnl)

    # for value in enumerate(all_pnl):
    #      if value== deficit_amt:
    #         day= profit_and_loss()[value][0]


    # if all_pnl[0]> all_pnl[1]:
    #     deficit_amount= all_pnl[0]- all_pnl[1]
    # print(deficit_amount)
        
    # for larger_fig in all_pnl[4]:
    #     if larger_fig:
    #         print(larger_fig)

pnl_write()