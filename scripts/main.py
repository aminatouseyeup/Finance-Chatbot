from finance_api import get_stock_data, display_stock_data, plot_close_prices


if __name__ == "__main__":
    API_KEY = "XHSCFMUSA223FUU5"
    symbol = input("Entrez le symbole boursier : ")

    stock_data = get_stock_data(symbol, API_KEY, interval="5min")
    if stock_data:
        display_stock_data(stock_data)
        plot_close_prices(stock_data)
    else:
        print("Aucune donnée disponible.")
