import get_stock_data from finance_api

api_key = 'XHSCFMUSA223FUU5'
symbol = input("Entrez le symbole boursier : ")
stock_data = get_stock_data(symbol, api_key)
print(stock_data)