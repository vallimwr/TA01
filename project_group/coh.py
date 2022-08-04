from pathlib import Path
import re, csv

file_path = Path.cwd()/'project_group'/'overall_report.txt'
# set file path to overall_report.txt
file_path.touch()
# use touch function to create file

def cash_on_hand():
    '''
    - to read and append for cash on hand
    '''
    coh_list = []
# create an empty_list to append items from cash on hand csv
    path = Path.cwd()/'project_group'/'csv_reports'/'cash-on-hand-usd.csv'
# set file path to cash on hand csv
    with path.open(mode = "r",encoding="UTF-8",newline="") as file:#
        reader = csv.reader(file)
# assign readers
        next(reader)
# skip line to read data in csv file
        for line in reader:
            coh_list.append(line)
# append data in csv to empty list
        return coh_list
        
#print(cash_on_hand())

def cashonhand_write(forex):
    '''
    - The function will calculate the difference in the cash on hand and 
      convert it to SGD using the real time exchange rate
    - the function will highlight the day where cash on hand is lower than the previous day and the value difference
      in summary_report.txt.
    '''
    all_coh = []
# make empty list for the data of amount of cash each day from cash on hand csv
    day_list = []
# make empty list for the days from the cash on hand csv
    for value in cash_on_hand():
# for each value in the csv file
        all_coh.append(float(value[1])*forex)
# appends amount of cash each day and convert it from USD to SGD to empty list
    #print(all_coh)

    for days in cash_on_hand():
# for each day in the csv file
        day_list.append(days[0])
# append days in csv file to empty list
    #print(day_list)

    count = 0 
# set a global counter
    for amount in range(len(all_coh)-1):
# for each amount except the last
        diff = all_coh[amount] - all_coh[amount + 1]
# calculate difference in cash on hand amount between each day
        if diff >0:

            with file_path.open(mode = 'a', encoding = 'UTF-8') as file:
                text = file.write(f"[CASH DEFICIT] DAY: {day_list[amount+1]}, AMOUNT: SGD{diff:.2f}\n")

                count += 1

    if count == 0:
        with file_path.open(mode = 'a', encoding = 'UTF-8') as file:
                text = file.write(f"[CASH SURPLUS] Cash-on-hand on each period is higher than the previous period\n")
