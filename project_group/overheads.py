from pathlib import Path
import re, csv

file_path = Path.cwd()/'project_group'/'overall_report.txt'
file_path.touch()


try:
    def overheads():
        """
        - This function returns the data in the overheads csv file 
        - It reads the values in  the overhead csv and appends it to an empty list
        """
        #Empty list made to store overhead values
        overheads_list= []
        path = Path.cwd()/'project_group'/'csv_reports'/'Overheads.csv'
        with path.open(mode= "r", encoding= "UTF-8") as file:
            reader= csv.reader(file)
            #skips the headers in the overheads csv 
            next (reader)

            #appends values without the headers in the overheads csv to the overheads_list
            for line in reader:
                overheads_list.append(line)
            return overheads_list
except Exception as e:
    # errorhandling to to test that code works
    print(f"This does not work. Reason: {e}")

##check values in overheads()        
#print(overheads())

try:
    def overheads_write():
        """
        - This function returns the highest overhead category and amount in the overheads csv
        - It appends the overhead values in an empty list and finds the highest overhead  
        """
        # empty list made to append overhead values 
        all_overheads= []
        # for loop to append values in the index position of 1
        for value in overheads():
            all_overheads.append(float(value[1]))
        
        # max() used to find the highest amount
        highest_amt= max(all_overheads)
        
        # used to find the category that the highest amount belongs to
        for number, values in enumerate(all_overheads):
            if values== highest_amt:
                category= overheads()[number][0]
                with file_path.open(mode = 'a', encoding = 'UTF-8') as file:
                    text = file.write(f"[HIGHEST OVERHEADS] {category}: {highest_amt}\n")

except Exception as e:
    #errorhandling to test if the code works
        print(f"This does not work. Reason: {e}")