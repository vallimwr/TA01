import requests
from pathlib import Path

api_key = "1JZVGRKCHDT3KUSQ"
# assign api key to the variable api_key
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
# assign api url to the variable url
r = requests.get(url)
# request access for data using the function .get and assign it to the variable response
data = r.json()
# retrieve data with the function .json from response and save it as data

#print(data)

file_path = Path.cwd()/'project_group'/'overall_report.txt'
# set file path to overall_report.txt
file_path.touch()
# use touch function to create the file 

def api():
    '''
    - This function extracts the real time currency exchange rate for USD to SGD from AlphaVantage
    - The exchange rate will then be written in overall_report.txt
    '''
    forex = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
# index exchange rate in data and convert to float before assigning to forex
    with file_path.open(mode = 'w', encoding = 'utf-8') as file:
# write exchange rate in summary_report.txt 
        if file_path.exists():
            value = file.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD 1 = SGD{forex}\n")
    return forex