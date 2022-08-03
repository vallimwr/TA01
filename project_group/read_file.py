<<<<<<< HEAD
=======

>>>>>>> 12bbc18605d974e2b3c0d32276c9818a1fc9891d
from pathlib import Path
import re, csv

def overheads():

    overhead_list = []
    path = Path.cwd()/'project_group'/'csv_reports'/'Overheads.csv'
    with path.open(mode= "r", encoding= "UTF-8") as file:
<<<<<<< HEAD
        reader= csv.reader(file)

        for value in reader:
            overhead_list.append(value)
        
        return overhead_list


    
=======
                reader= csv.reader(file)
                next(reader)
                for line in reader:
                    
                    print(line)


print(overheads())
>>>>>>> 12bbc18605d974e2b3c0d32276c9818a1fc9891d

# blank_list = []

# def cash_on_hand():
#      path = Path.cwd()/'project_group'/'csv_reports'/'cash-on-hand-usd.csv'
#      with path.open(mode = "r",encoding="UTF-8",newline="") as file:
#         reader = csv.reader(file)
#         next(reader)

#         for line in reader:
#             for value in line:
#                 blank_list.append(float(value))

#             print(blank_list)