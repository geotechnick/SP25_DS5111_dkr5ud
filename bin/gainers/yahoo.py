from base import GainerBase
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
        tickers = ["AAPL", "MSFT", "NVDA"]
        data = yf.download(tickers, period="1d", interval="1m", progress=False, group_by='ticker')
        self.data = data  # Store the data for further processing

    def normalize(self):
        print("Normalizing Yahoo gainers data...")
        # Example normalization logic
        self.normalized_data = self.data  # In a real case, normalization logic would go here

    def save_with_timestamp(self):
        print("Saving Yahoo gainers data with timestamp...")
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        results = []

        for symbol in self.data:
            df = self.data[symbol]
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

        df = pd.DataFrame(results)
        file_exists = os.path.isfile('gainers_output.csv')
        df.to_csv('gainers_output.csv', mode='a', header=not file_exists, index=False)
        print(f"Data saved to gainers_output.csv.")