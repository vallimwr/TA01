# import requests

<<<<<<< HEAD
def forex(USD):
    api_key = "1JZVGRKCHDT3KUSQ"
    url = "https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey={api_key}"

    r = requests.get(url)
    data = r.json()

    exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    print(exchange_rate)
=======
# api_key = "1JZVGRKCHDT3KUSQ"
# url = "https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey={api_key}"

# r = requests.get(url)
# data = r.json()

# exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
# print(exchange_rate)
>>>>>>> 12bbc18605d974e2b3c0d32276c9818a1fc9891d
