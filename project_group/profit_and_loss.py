#from api import forex
from pathlib import Path
import re, csv

file_path = Path.cwd()/'project_group'/'overall_report.txt'
file_path.touch()

def profit_and_loss():
    """
    - This function returns the data in the profit and loss csv
    - It reads the values in the profit and loss csv and appends it to an empty list
    """
    # empty list made to append the net profit values
    pnl_list = []
    path = Path.cwd()/'project_group'/'csv_reports'/'profit-and-loss-usd.csv'
    # path is opened in read mode as file
    with path.open(mode = "r",encoding="UTF-8-sig",newline="") as file:
        reader = csv.reader(file)
        # skips headers in the profit and loss csv
        next(reader)
        
        #for loop used to append values without the headers in the profit and loss csv to pnl_list
        for line in reader:
            pnl_list.append(line)
        return pnl_list

## Check values in profit and loss
#print(profit_and_loss())

def pnl_write(forex): 
    """
    - This function  returns the days that have deficit and the amount of deficit of the net profit
    - If there are no deficits, the function will return a surplus
    - The net profit values and the days are added to separate empty lists
    """
    #empty lists made to append the net profit values and days respectively
    all_pnl= []
    day_pnl= []

    #for loop to append the net profit values in index position 4
    #values are converted to float
    for value in profit_and_loss():
        all_pnl.append(int(value[4]*int(forex)))
    # to check the values in all_pnl
    #print(all_pnl)

    #for loop to append the days in index position 0
    for days in profit_and_loss():
        day_pnl.append(days[0])
    # to check the values in all_pnl
    #print(day_pnl)
    
    count = 0 
    #for loop to 
    for amount in range(len(all_pnl)-1):
        diff = all_pnl[amount] - all_pnl[amount + 1]
        if diff >0:
            with file_path.open(mode = 'a', encoding = 'UTF-8') as file:
                text = file.write(f"[PROFIT DEFICIT] DAY: {day_pnl[amount+1]}, AMOUNT: SGD{diff:.2f}\n")
# write cash deficit with corresponding day and difference in overall_report.txt
                count += 1

    if count == 0:
        with file_path.open(mode = 'a', encoding = 'UTF-8') as file:
                text = file.write(f"[PROFIT SURPLUS] Profit on each period is higher than the previous period\n")
# write cash surplus in overall_report.txt