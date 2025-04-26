from bin.gainers.base import GainerBase
import yfinance as yf
import pandas as pd
import os
from datetime import datetime

# Yahoo gainer implementation
class GainerYahoo(GainerBase):
    def __init__(self, url):
        super().__init__(url)

    def download(self):
        print("Downloading Yahoo gainers data...")
        # Example of downloading Yahoo finance data
        self.tickers = ["AAPL", "MSFT", "NVDA"]
        self.data = yf.download(self.tickers, period="1d", interval="1m", progress=False, group_by='ticker')

    def normalize(self):
        print("Normalizing Yahoo gainers data...")
        # In a real case, normalization logic would go here
        self.normalized_data = self.data

    def save_with_timestamp(self):
        print("Saving Yahoo gainers data with timestamp...")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        results = []

        # Handle single vs multiple tickers
        if isinstance(self.tickers, str):
            tickers_list = [self.tickers]
        else:
            tickers_list = self.tickers

        for symbol in tickers_list:
            try:
                if len(tickers_list) == 1:
                    df = self.data  # Single ticker: no MultiIndex
                else:
                    df = self.data[symbol]

                if df.empty:
                    print(f"No data for {symbol}, skipping...")
                    continue

                latest = df.iloc[-1]
                open_price = df.iloc[0]['Open']
                last_price = latest['Close']
                price_change = last_price - open_price
                price_percent_change = (price_change / open_price) * 100

                results.append({
                    'timestamp': timestamp,
                    'symbol': symbol,
                    'price': round(last_price, 2),
                    'price_change': round(price_change, 2),
                    'price_percent_change': round(price_percent_change, 2),
                })

            except Exception as e:
                print(f"Error processing {symbol}: {e}")

        if results:
            df_results = pd.DataFrame(results)
            file_exists = os.path.isfile('gainers_output.csv')
            df_results.to_csv('gainers_output.csv', mode='a', header=not file_exists, index=False)
            print("Data saved to gainers_output.csv.")
        else:
            print("No results to save.")

