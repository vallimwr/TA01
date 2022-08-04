import requests
from pathlib import Path

api_key = "1JZVGRKCHDT3KUSQ"
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

r = requests.get(url)
data = r.json()

print(data)

file_path = Path.cwd()/'project_group'/'overall_report.txt'
file_path.touch()

def api():
    forex = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    with file_path.open(mode = 'w', encoding = 'utf-8') as file:
        if file_path.exists():
            value = file.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD 1 = SGD{forex}")

        else:
            print('does not exist')
        return forex

print(api()) 