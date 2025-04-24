from abc import ABC, abstractmethod

# FACTORY
class GainerFactory:
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj', 'test'], f"Unrecognized gainer type {choice}"
        self.choice = choice 

    def get_downloader(self):
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()

    def get_processor(self):
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        elif self.choice == 'wsj':
            return GainerProcessWSJ()

# DOWNLOADER
class GainerDownload(ABC):
    def __init__(self):
        self.url = url

    @abstractmethod
    def download(self):
        pass

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        pass
        

    def download(self):
        print("Downloading yahoo gainers")

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        pass

    def download(self):
        print("Downloading WSJ gainers")




# PROCESSORS 
class GainerProcess(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def normalize(self):
        pass

    @abstractmethod
    def save_with_timestamp(self):
        pass

class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        pass

    def normalize(self):
        print("Normalizing yahoo gainers")
        
    import yfinance as yf
    import pandas as pd
    import os
    from datetime import datetime

    def fetch_latest_stock_data(tickers):
        # Download 1 day of 1-minute interval data
        data = yf.download(tickers, period="1d", interval="1m", progress=False, group_by='ticker')

        results = []

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        for symbol in tickers:
            try:
                df = data[symbol]
                if df.empty:
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
                print(f"Failed to fetch data for {symbol}: {e}")

        return results

    def save_to_csv(data, filename='gainers_output.csv'):
        df = pd.DataFrame(data)
        file_exists = os.path.isfile(filename)

        df.to_csv(filename, mode='a', header=not file_exists, index=False)
        print(f"{'Appended' if file_exists else 'Created'} {len(df)} rows to {filename}")

    if __name__ == "__main__":
        # Example tickers – replace or fetch dynamically
        tickers = ["AAPL", "MSFT", "NVDA"]
        gainers_data = fetch_latest_stock_data(tickers)
        save_to_csv(gainers_data)

    def save_with_timestamp(self):
        print("Saving Yahoo gainers")
# ITS OWN SEPARATE FILE

# TEMPLATE
class ProcessGainer:
    def __init__(self, gainer_downloader, gainer_normalizer):
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        self.downloader.download()

    def _normalize(self):
        self.normalizer.normalize()

    def _save_to_file(self):
        self.normalizer.save_with_timestamp()

    def process(self):
        self._download()
        self._normalize()
        self._save_to_file()

if __name__=="__main__":
    # Our sample main file would look like this
    import sys
   
    # Make our selection, 'one' choice
    choice = sys.argv[1]

    # let our factory get select the family of objects for processing
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    # create our process
    runner = ProcessGainer(downloader, normalizer)
    runner.process()




