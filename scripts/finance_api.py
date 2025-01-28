import requests
import pandas as pd
import matplotlib.pyplot as plt


def get_stock_data(symbol, api_key, interval="5min"):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': interval,
        'apikey': api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if "Time Series (" + interval + ")" in data:
        return data["Time Series (" + interval + ")"]
    else:
        print("Erreur ou données non disponibles :", data.get("Note") or data.get("Error Message"))
        return None

def display_stock_data(data):
    for timestamp, values in list(data.items())[:5]:  # display 5 first entries
        print(f"{timestamp}: {values}")

def plot_close_prices(data):
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df.rename(columns={
        '1. open': 'Open',
        '2. high': 'High',
        '3. low': 'Low',
        '4. close': 'Close',
        '5. volume': 'Volume'
    })
    df['Close'] = df['Close'].astype(float)
    df['Close'].plot(title="Prix de clôture", figsize=(10, 6))
    plt.show()

