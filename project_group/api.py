import requests
from pathlib import Path

api_key = "1JZVGRKCHDT3KUSQ"
url = "https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey={api_key}"

r = requests.get(url)
data = r.json()

file_path = Path.cwd()/'project group'/'overall_report.txt'
file_path.touch

def api_func():
    forex = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    with file_path.open(mode = 'w', encoding = 'utf-8') as file:
        value = file.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD 1 = SGD{forex}")
    return value
print(api_func())