#from api import forex
from pathlib import Path
import re, csv

file_path = Path.cwd()/'project_group'/'overall_report.txt'
file_path.touch()

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

def cashonhand_write():
    all_coh = []
    day_list = []
    for value in cash_on_hand():
        all_coh.append(float(value[1]))
    print(all_coh)

    for days in cash_on_hand():
        day_list.append(days[0])
    print(day_list)
#cashonhand_write()

    count = 0 
    for amount in range(len(all_coh)-1):
        diff = all_coh[amount] - all_coh[amount + 1]
        if diff >0:
            with file_path.open(mode = 'w', encoding = 'UTF-8') as file:
                text = file.write(f"[CASH DEFICIT] DAY: {day_list[amount+1]}, AMOUNT: SGD{diff:.2f}")
                count += 1

        else:
            print('does not exist')

    if count == 0:
        with file_path.open(mode = 'w', encoding = 'UTF-8') as file:
                text = file.write(f"[CASH SURPLUS] Cash-on-hand on each period is higher than the previous period")

    else:
        print('does not exist')

cashonhand_write()