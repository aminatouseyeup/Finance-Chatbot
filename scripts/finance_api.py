import requests

def get_stock_data(symbol, api_key):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

