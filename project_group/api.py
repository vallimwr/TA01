import requests
from pathlib import Path

def forex(USD):
    api_key = "1JZVGRKCHDT3KUSQ"
    url = "https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey={api_key}"

    r = requests.get(url)
    data = r.json()

    file_path = Path.cwd()/'project group'/'overall_report.txt'

