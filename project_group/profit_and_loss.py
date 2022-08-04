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
    day_pnl= []
    for value in profit_and_loss():
        all_pnl.append(float(value[4]))
    print(all_pnl)

    for days in profit_and_loss():
        day_pnl.append(days[0])
    print(day_pnl)

    count = 0 
    for amount in range(len(all_pnl)-1):
        diff = all_pnl[amount] - all_pnl[amount + 1]
        if diff >0:
            with file_path.open(mode = 'w', encoding = 'UTF-8') as file:
                text = file.write(f"[CASH DEFICIT] DAY: {day_pnl[amount+1]}, AMOUNT: SGD{diff:.2f}")
                count += 1
        else:
            print("what")

        if count == 0:
            with file_path.open(mode = 'w', encoding = 'UTF-8') as file:
                    text = file.write(f"[PROFIT SURPLUS] Profit on each period is higher than the previous period")

        else:
            print('does not exist')


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