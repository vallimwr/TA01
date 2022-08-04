from pathlib import Path
import re, csv

file_path = Path.cwd()/'project_group'/'overall_report.txt'
file_path.touch()


try:
    def overheads(forex):
        """
        This function reads the values in  the overhead csv and appends it to an empty list
        """
        #Empty list made to store overhead values
        overheads_list= []
        path = Path.cwd()/'project_group'/'csv_reports'/'Overheads.csv'
        with path.open(mode= "r", encoding= "UTF-8") as file:
            reader= csv.reader(file)
            #skips the headers in the overheads csv 
            next (reader)

            #appends values in the overheads csv to the overheads_list
            for line in reader:
                overheads_list.append(line)
            return overheads_list
    print("This is working")
except Exception as e:
    # errorhandling to to test that code works
    print(f"This does not work. Reason: {e}")

##check values in overheads()        
#print(overheads())

try:
    def overheads_write():
        all_overheads= []
        for value in overheads():
            all_overheads.append(float(value[1]))

        highest_amt= max(all_overheads)
        

        for number, values in enumerate(all_overheads):
            if values== highest_amt:
                category= overheads()[number][0]
        return f"[HIGHEST OVERHEADS] {category}: {highest_amt}"
            
    print("This is working")
except Exception as e:
        print(f"This does not work. Reason: {e}")

print(overheads_write())